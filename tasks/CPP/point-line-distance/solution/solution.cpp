// Solution.cpp
//---------------------------------------------------------------------------

#include <cmath>

using namespace std;
//--------------------------------------------------------------------------

double distance(int x1, int y1, int x2, int y2, int x, int y)
{
	int A =   y2 - y1;
	int B = -(x2 - x1);
	int C = -B * y1 - A * x1;

	return abs((double)A * x + B * y + C) / sqrt(A * A + B * B);
}
//--------------------------------------------------------------------------
