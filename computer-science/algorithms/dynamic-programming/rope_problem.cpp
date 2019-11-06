// Rope problem implementation comparison.
// Credit: github.com/nemosx for the rope_func1 implementation.

#include <iostream>
#include <vector>
#include <chrono>

using namespace std;

// Nemosx's implementation
int rope_func1(int n)
{
	vector<int> opt(n+1, 0);
	opt[1] = 1;

	for (int i = 2; i <= n; ++i)
		for (int k = 1; k < i; ++k)
			opt[i] = max(opt[i], max(opt[k] * (i - k), k * (i - k)));

	return opt[n];
}

// My implementation
int rope_func2(int n)
{
	vector< vector<int> > table(n, vector<int>(n+1));

	// base case opt[1, m] = m - 1
	for (int j = 2; j <= n; j++)
		table[1][j] = j - 1;

	for (int i = 2; i < n; i++)
		for (int j = i + 1; j <= n; j++)
			table[i][j] = max(i*(j-i), max(table[i-1][j], i * table[i][j-i]));

	return table[n-1][n];
}

// Calculate average run time of both implementations.
void timeit(int n)
{
	auto start1 = chrono::high_resolution_clock::now();
	for (int i = 0; i < 1000; i++)
		rope_func1(n);
	auto end1 = chrono::high_resolution_clock::now();
	chrono::duration<double> duration1 = end1 - start1;

	auto start2 = chrono::high_resolution_clock::now();
	for (int i = 0; i < 1000; i++)
		rope_func2(n);
	auto end2 = chrono::high_resolution_clock::now();
	chrono::duration<double> duration2 = end2 - start2;

	cout << "Run time of function 1: " << duration1.count() / 1000 << " seconds" << endl;
	cout << "Run time of function 2: " << duration2.count() / 1000 << " seconds" << endl;
}

int main() {
	int n;
	cout << "Enter an integer larger than 2: ";
	cin >> n;
	cout << endl;
	
	int result1 = rope_func1(n);
	int result2 = rope_func2(n);
	cout << "Function 1 result: " << result1 << endl;
	cout << "Function 2 result: " << result2 << endl;
	timeit(n);
	cout << endl;

	return 0;
}
