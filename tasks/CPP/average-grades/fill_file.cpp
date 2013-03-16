// FillFile.cpp
// !!!!!!!!!!!!!ÅÑËÈ ÂÄÐÓÃ ÇÀÕÎ×ÅØÜ ÈÇÌÅÍÈÒÜ ÒÅÑÒÛ!!!!!!!!!!!!!!!!!!!!
//--------------------------------------------------------------------------

#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <cstring>

using namespace std;
//--------------------------------------------------------------------------

struct Student
{
    Student(char *lN, int gr, double gpa)
    {
        memset(lastName, 0, 20);
        strcpy(lastName, lN);
        group = gr;
        this->gpa = gpa;
    }

    char lastName[20];

    int    group;
    double gpa;
};
//--------------------------------------------------------------------------

void writeBinary(const std::vector<Student>& students, const char* filename) {
    int n = students.size();
    ofstream out(filename, ios::binary | ios::out);
    out.write(reinterpret_cast<const char*>(&n), 4);
    for (int i = 0; i < students.size(); i++) {
        const Student& st = students[i];
        out.write(st.lastName, 20);
        out.write(reinterpret_cast<const char*>(&st.group), 4);
        out.write(reinterpret_cast<const char*>(&st.gpa), 8);
    }
    out.close();
}

void writeText(const std::vector<Student>& students, const char* filename) {
    int n = students.size();
    ofstream out(filename, ios::out);
    out << n << endl;
    for (int i = 0; i < students.size(); i++) {
        const Student& st = students[i];
        out << st.lastName << " " << st.group << " " << st.gpa << endl;
    }
    out.close();
}

int main() {
    std::vector<Student> students;
    students.push_back(Student("Ivanov",      1,  7.5));
    students.push_back(Student("Petrova",     1,  10.0));
    students.push_back(Student("Sidorov",     1,  4.5));
    students.push_back(Student("Oleinikov",   5,  8.4));
    students.push_back(Student("Zadvorniy",   2,  9.5));
    students.push_back(Student("Mazanik",     3,  10.0));
    students.push_back(Student("Sergeev",     1,  6.7));
    students.push_back(Student("Pavlov",      1,  7.1));
    students.push_back(Student("Egorov",      9,  4.0));
    students.push_back(Student("Byhina",      8,  7.4));
    students.push_back(Student("Havavakina",  1,  5.2));
    students.push_back(Student("Abvgdeikina", 5,  5.2));
    writeBinary(students, "03.bin");
    writeText(students, "03.txt");

    return 0;
}
//--------------------------------------------------------------------------
