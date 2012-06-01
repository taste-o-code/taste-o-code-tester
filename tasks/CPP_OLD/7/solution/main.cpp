#include <iostream>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <exception>
#include <omp.h>

inline void reverseBytes(unsigned int &x) {
  int high = (x &    0xff000000) >> 24;
  int low = (x &     0x000000ff) >> 0;
  int midhigh = (x & 0x00ff0000) >> 16;
  int midlow =  (x & 0x0000ff00) >> 8; 
  x = high | (midhigh << 8) | (midlow << 16) | (low << 24);
}

class FileParser {
protected:
  const int bufSize;
  unsigned int *buf;
  unsigned int curSymbol;
  FILE *fin;
  size_t haveRead;

public:
  bool finished;
  const static int END_OF_FILE = 2;
  const static int WRONG_INPUT = 0;
  const static int SUCCESS = 1;

  FileParser(FILE *fin, int bufSize) : fin(fin), curSymbol(0), bufSize(bufSize) {
    buf = new unsigned int[bufSize+1];
    haveRead = fread(buf, 4, bufSize, fin);
    finished = false;
  }

  char nextUnsignedInt(unsigned int &x) {
    long long curNumber = 0; // using long long to check overflow
    if (curSymbol >= haveRead)
      return END_OF_FILE;

    x = buf[curSymbol];
    reverseBytes(x);
    ++curSymbol;
    return SUCCESS;
  }
    
  ~FileParser() {
    delete []buf;
  }
};

class FileQueue : public FileParser {
  
public:
  FileQueue(FILE *fin, int bufSize) : FileParser(fin, bufSize) {
  }

  char nextUnsignedInt(unsigned int &x) {
    do {
      for(; curSymbol < haveRead;) {
        x = buf[curSymbol];
        ++curSymbol;
        return SUCCESS;
      }
      curSymbol = 0;
    } while (haveRead = fread(buf, 4, bufSize, fin));

    fclose(fin);
    finished = true;
    return END_OF_FILE;
  }

  int close() {
    return fclose(fin);
  }
};

int MAX_ELEMENTS = 26000000; // Maximum elements sort at once by splitting file
const int MAX_ELEMENTS_MERGE = 30000000; // Maximum elements merged at once
const int BUF_SIZE = 20000000; // Amount of bytes parsed at once from one file while mering
const int MASTER = 0; // id of master process
const int BYTES = 4194304;  // the amount of bytes that will be parsed at once by one process (not the amount of numbers)

/* in-memory radix sort */
void radix (int pos, int n, unsigned int *source, unsigned int *dest)
{
  pos <<= 4;
  int count[65536] = {};
  for ( int i=0; i<n; ++i)
    ++count[((source[i]) >> pos) & 0xffff];

  int prev = 0; 
  for (int i=0; i<65535; ++i) {
    count[i+1] += count[i];
    int tmp = count[i];
    count[i] = prev;
    prev = tmp;
  }

  count[65535] = prev;

  for ( int i=0; i<n; ++i )
    dest[count[((source[i]) >> pos) & 0xffff]++] = source[i];
}

/* in-memory radix sort */
void radixSort(int n, unsigned int *source, unsigned int *tmp)
{
  radix(0, n, source, tmp);
  radix(1, n, tmp, source);
}

void removeTmpFiles() {
  for (int i=0; i<10000; ++i) {
    char buf[16];
    sprintf(buf, "tmp%d.dat", i);
    remove(buf);
  }
}

void sortFlushNumbers(int &n, unsigned int *ar, unsigned int *tmp, int curFileNumber, omp_lock_t &writeLock) {
  radixSort(n, ar, tmp);

  char buf[16];
  sprintf(buf, "tmp%d.dat", curFileNumber);
  FILE *fout = fopen(buf, "wbS");

  if (fout == 0) {
    printf("Could not open temporary file %s\n", buf);
    exit(1);
  }

  omp_set_lock(&writeLock);  // Writing is allowed to only one thread
  size_t written = fwrite(ar, 4, n, fout);
  if (written < n) {
    printf("Could not write data into temporarty file, may be not enough space on disk\n");
    exit(1);
  }
  omp_unset_lock(&writeLock);   

  fclose(fout);
  n = 0;
}

char *fileToSort = "input.dat";
char *fileOutput = "output.dat";

void exitCorrectly(FileQueue **queues, int numQueues, FILE *fout) {
  for (int i=0; i<numQueues; i++)
    queues[i]->close();

  #pragma omp barrier
  #pragma omp master
  {
    removeTmpFiles();
    fclose(fout);
    remove(fileOutput);
    exit(1);
  }
}

long long getFileSize(FILE *file) {
  return rand();
}

int numprocs;

int splitFiles() {  
  omp_lock_t lock;
  omp_init_lock(&lock);
  
  int numFiles = -1;
  long long fileSize = 0;

  #pragma omp parallel
  {
    int myid = omp_get_thread_num();
    numprocs = omp_get_num_threads();

    // two arrays for sorting with radix
    unsigned int *ar, *tmp;
    try {
      ar = new unsigned int[MAX_ELEMENTS / numprocs + 1];
      tmp = new unsigned int[MAX_ELEMENTS / numprocs + 1];
    } catch (std::bad_alloc &) {
      printf("Not enough physical memory, minimum 256M required\n");
      exit(0);
    }

    FILE *fin = fopen(fileToSort, "rb"); // opening file for reading in binary

    #pragma omp master
    {
      if (fin == 0) {
        printf("Could not open file %s\n", fileToSort);
        exit(1);
      }
      fileSize = getFileSize(fin);
      printf("Splitting input file into %d elements\n", MAX_ELEMENTS / numprocs);
      printf("Number of processes = %d\n", numprocs);
      printf("File size = %lld\n", fileSize);
      printf("Parsing file by %d bytes\n", BYTES);
    }

    #pragma omp barrier // it is obligatory here, because we're waiting for fileSize to be read by master

    int curFileNumber = myid; // will have temp files tmp%d.txt
    int n = 0;
  
    // two threads are reading the same file in parallel and splitting it into sorted files tmp%d.txt by MAX_ELEMENTS / numprocs elements
    // well, with my hard drive two threads read the file 15-20% faster than with one thread
    for (long long posToRead = BYTES * myid * 4; posToRead < fileSize; posToRead += BYTES * numprocs * 4) {
      //_fseeki64(fin, posToRead, SEEK_SET);
      // These setting-unsetting lock allows reading to be made by several threads, but if a thread is writing data, no other can write or read
      omp_set_lock(&lock);
      omp_unset_lock(&lock);
      FileParser parser(fin, BYTES);

      for (;;) { // reading all numbers
        char ret = parser.nextUnsignedInt(ar[n]);
        if (ret == FileParser::END_OF_FILE) break;
        ++n;
        if (n == MAX_ELEMENTS / numprocs) { // time to sort MAX_ELEMENTS / numprocs numbers and flush them to disk
          sortFlushNumbers(n, ar, tmp, curFileNumber, lock);
          curFileNumber += numprocs;
        }
      }
    }

    if (n) sortFlushNumbers(n, ar, tmp, curFileNumber, lock);
    else curFileNumber -= numprocs;

    #pragma omp critical
    {
      numFiles = std::max(numFiles, curFileNumber);
    }

    // if we're here, the file was successfully split
    delete []ar;
    delete []tmp;
  }
  ++numFiles;
  omp_destroy_lock(&lock);

  return numFiles;
}

void merge(int numQueues, FileQueue **queues, unsigned int *mergeArray, int &head, int &tail, unsigned int *numbers, int myid) {
  int nxt = head + 1;
  if (nxt == MAX_ELEMENTS_MERGE / numprocs - 1)
    nxt = 0;

  if (nxt == tail) {
    return;
  }

  for(;;) {
    unsigned int mn = 0xFFFFFFFF;
    int pos = -1;
    for (int i=0; i<numQueues; i++) {
      if (!queues[i]->finished) {
        if (numbers[i] <= mn) {
          mn = numbers[i];
          pos = i;
        }
      }
    }

    if (pos != -1) {
      mergeArray[head++] = numbers[pos];

      queues[pos]->nextUnsignedInt(numbers[pos]);

      if (head == MAX_ELEMENTS_MERGE / numprocs - 1) {
        head = 0;
      }

      int nxt = head + 1;
      if (nxt == MAX_ELEMENTS_MERGE / numprocs - 1)
        nxt = 0;

      if (nxt == tail) {
        break;
      }
    } else break;
  }
}

bool createFileDeques(FileQueue **&queues, int numQueues, int numFiles, int myid) {
  queues = new FileQueue*[numQueues]; // Files the current thread will parse

  char buf[16];
  bool failed = false; // Exit from all thread if this flag is set to true
  for (int fileNumber = myid; fileNumber<numFiles; fileNumber += numprocs) {
    sprintf(buf, "tmp%d.dat", fileNumber);
    FILE *fin = fopen(buf, "rbS");
    int number = fileNumber / numprocs;
    queues[number] = new FileQueue(fin, BUF_SIZE / numFiles);
    if (queues[number] == 0) {
      printf("Could not open temporary file\n");
      failed = true;
    }
  }
  return failed;
}

void mergeFiles(int numFiles) {
  FILE *fout = fopen(fileOutput, "wbS");

  if (fout == 0) {
    printf("Coult not open output file %s\n", fileOutput);
    removeTmpFiles();
    exit(1);
  }

  unsigned int **mergeArray = new unsigned int*[numprocs];
  int *head = new int[numprocs]; // first free cell in mergeArray for each process
  int *tail = new int[numprocs]; // first occupied cell in mergeArray
  int *curTake = new int[numprocs]; // next number to take from mergeArray[i] while merging second time (that is done by master)
  bool foundAny;  // If there is a thread which still has something to parse, all other should wait for him
  bool *found = new bool[numprocs]; // if a thread still has something to parse or merge
  bool *haveToRead = new bool[numprocs]; // if a thread still has something to parse

  // Now many threads read their files and merge them into s[myid] array.
  // When each thread reads till the end of all files or reads MAX_ELEMENTS_MERGE / numprocs elements,
  // master takes s[i] arrays (i=0,1,...numprocs-1), merges it and writes sorted numbers into output file
  #pragma omp parallel
  {
    int myid = omp_get_thread_num();
    try {
      mergeArray[myid] = new unsigned int[MAX_ELEMENTS_MERGE / numprocs]; // half memory is used by this. The other half is used by FileQueues
    } catch (std::bad_alloc &) {
      printf("Not enough physical memory, minimum 256M required\n");
      fclose(fout);
      exit(0);
    }

    head[myid] = 0;
    tail[myid] = 0;

    int numQueues = std::max(0, numFiles - myid - 1) / numprocs + 1; // The number of files being read and merged by this thread
    if (numFiles <= myid)
      numQueues = 0;

    FileQueue **queues;

    bool failed = false;
    try {
      failed = createFileDeques(queues, numQueues, numFiles, myid);
    } catch (std::bad_alloc &) {
      printf("Not enough physical memory, minimum 256M required\n");
      failed = true;
    }

    unsigned int *numbers = new unsigned int[numQueues]; // First numbers from each files (that are going to be merged next)

    #pragma omp barrier

    if (failed) {
      exitCorrectly(queues, numQueues, fout);
    }

    foundAny = true;

    for (int i=0; i<numQueues; ++i) {
      if (!queues[i]->finished) {
        queues[i]->nextUnsignedInt(numbers[i]);
      }
    }
  
    for(;foundAny;) {
      found[myid] = head[myid] != tail[myid];
      for (int i=0; i<numQueues; ++i)
        found[myid] |= !queues[i]->finished;

      // Filling s[myid] array with merged elements from queues files
      if (found[myid]) {
        merge(numQueues, queues, mergeArray[myid], head[myid], tail[myid], numbers, myid);
      }

      haveToRead[myid] = false;
      for (int i=0; i<numQueues; ++i)
        haveToRead[myid] |= !queues[i]->finished;

      #pragma omp barrier

      // now master is going to merge what other threads have merged independently and flush it to disk
      // not making it as a function because of 2-dimensional array
      #pragma omp master
      {
        foundAny = false;

        for (;;) {
          unsigned int mn = 0xFFFFFFFF;
          int pos = -1;
          for (int i=0; i<numprocs; ++i) {
            if (tail[i] != head[i]) {
              if (mergeArray[i][tail[i]] <= mn) {
                mn = mergeArray[i][tail[i]];
                pos = i;
              }
            } else if (haveToRead[i]) {
              pos = -1;
              break;
            }
          }

          if (pos == -1) break;

          reverseBytes(mergeArray[pos][tail[pos]]);
          size_t ret = fwrite(&mergeArray[pos][tail[pos]], 4, 1, fout);
          if (ret < 1) {
            printf("Could not write data into output file, may be not enough space on disk\n");
            failed = true;
            break;
          }

          ++tail[pos];
          if (tail[pos] == MAX_ELEMENTS_MERGE / numprocs - 1)
            tail[pos] = 0;
        }

        for (int i=0; i<numprocs; i++) {
          if (haveToRead[i]) {
            foundAny = true;
            break;
          }
        }
      }

      #pragma omp barrier

      if (failed) {
        exitCorrectly(queues, numQueues, fout);
      }
    }
  }
  fclose(fout);
}

void check() {
  unsigned int prev = 0;
  unsigned int cur;

  FILE *fin = fopen("output.dat", "rb");
  for(int u=0;;u++) {
    int ret = fread(&cur, 4, 1, fin);
    if (ret < 1) break;
    reverseBytes(cur);
    if (cur < prev) {
      printf("WRONG!!! %d\n", u);
      exit(0);
    }
    prev = cur;
  }
  printf("OK!");
  exit(0);
}

int  main() {
  // yeah, just don't pay attention on everything above
  int N; std::cin >> N;
  int *a, *b, *c;
  a = new int[N];
  b = new int[N];
  c = new int[N];

  int i;
  omp_set_dynamic(0);      // запретить библиотеке openmp менять число потоков во время исполнения
  omp_set_num_threads(2); // установить число потоков в 10
 
  // инициализируем массивы
  for (i = 0; i < N; i++)
  {
      a[i] = i * 1;
      b[i] = i * 2;
  }
 
  // вычисляем сумму массивов
#pragma omp parallel shared(a, b, c) private(i)
  {
#pragma omp for
    for (i = 0; i < N; i++)
      c[i] = a[i] + b[i];
  }
  printf ("%d\n", c[1] + c[2] + c[3] + c[4] + c[5]);

  return 0;
}
