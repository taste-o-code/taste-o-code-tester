// Solution.cpp
//--------------------------------------------------------------------------

#include <iostream>
#include <fstream>
#include <map>
#include <string>

using namespace std;
//--------------------------------------------------------------------------

void averageGrades(string fName)
{
    ifstream in(fName.c_str(), ios::binary | ios::in);

    map<int, double> groupMSum;
    map<int, int>    groupSCount;

    int    tempGr;
    double tempMark;
    int n = 0;

    in.read(reinterpret_cast<char*>(&n), 4);
    for (int i = 0; i < n; i++) {
        in.seekg(20, in.cur); // Skip last name, 20 bytes.
        in.read(reinterpret_cast<char*>(&tempGr),   4);
        in.read(reinterpret_cast<char*>(&tempMark), 8);

        groupMSum[tempGr] += tempMark;
        ++groupSCount[tempGr];
    }

    in.close();

    for (map<int, double>::iterator it = groupMSum.begin();
         it != groupMSum.end(); ++it)
	{
            double average = it->second / groupSCount[it->first];
            cout << it->first << " " << average << endl;
	}
}
//--------------------------------------------------------------------------


