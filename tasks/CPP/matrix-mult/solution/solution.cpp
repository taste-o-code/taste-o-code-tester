// Solution.cpp
//--------------------------------------------------------------------------

#include <algorithm>

using namespace std;
//--------------------------------------------------------------------------

int** mult(int** fMatrix, int** sMatrix, int size)
{
	int **result = new int*[size];
	for (int i = 0; i < size; ++i)
		result[i] = new int[size]();

	for (int i = 0; i < size; ++i)
		for (int j = 0; j < size; ++j)
			for (int k = 0; k < size; ++k)
				result[i][j] += fMatrix[max(i, k)][min(i, k)] *
								sMatrix[max(j, k)][min(j, k)];

	return result;
}
//--------------------------------------------------------------------------
