// Checker.cpp
//--------------------------------------------------------------------------

#include <iostream>

using namespace std;
//--------------------------------------------------------------------------

int** mult(int** a, int** b, int n);
//--------------------------------------------------------------------------

int main()
{
	int size; cin >> size;

	int **fMatrix = new int*[size];
	int **sMatrix = new int*[size];

	for (int i = 0; i < size; ++i)
	{
		fMatrix[i] = new int[i + 1];
		sMatrix[i] = new int[i + 1];
	}

	for (int i = 0; i < size; ++i)
		for (int j = 0; j < i + 1; ++j)
			cin >> fMatrix[i][j];

	for (int i = 0; i < size; ++i)
		for (int j = 0; j < i + 1; ++j)
			cin >> sMatrix[i][j];

	int **resMatrix = mult(fMatrix, sMatrix, size);

	for (int i = 0; i < size; ++i)
		for (int j = 0; j < size; ++j)
			cout << resMatrix[i][j] << " ";
}
//--------------------------------------------------------------------------
