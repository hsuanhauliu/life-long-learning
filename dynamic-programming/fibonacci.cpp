/* Author: Hsuan-Hau Liu
 * File: fibonacci.cpp
 * Desption: A demonstration of different implementations of fibanocci
 *           function.
 * Note: C+11 needed.
 */

#include <iostream>
#include <chrono>

using namespace std;

#define MAX 50

class Fibonacci
{

public:
	int fib_dc(int n);	// divide and conquer algorithm
	int fib_mem(int n);	// memoization implementation
	int fib_tab(int n);	// tabulation implementation
	void timeit(int n);

private:
	int fib_recurrence(int n, int table[]);
};


int Fibonacci::fib_dc(int n)
{
	if (n == 0 || n == 1)
		return 1;
	return fib_dc(n-1) + fib_dc(n-2);
}

int Fibonacci::fib_mem(int n)
{
	int table[MAX] = {0};	// table used for fib_mem function
	table[0] = table[1] = 1;
	return fib_recurrence(n, table);
}

// fac_mem helper function
int Fibonacci::fib_recurrence(int n, int table[])
{
	if (table[n] != 0)
		return table[n];
	else
		table[n] = fib_recurrence(n-1, table) + fib_recurrence(n-2, table);
	
	return table[n];
}

int Fibonacci::fib_tab(int n)
{
	int table[MAX] = {0};
	table[0] = table[1] = 1;

	for (int i = 2; i <= n; i++)
		table[i] = table[i-1] + table[i-2];

	return table[n];
}

// Run each function 1000 times and get the average time.
void Fibonacci::timeit(int n)
{
	chrono::duration<double> duration;

	auto start = chrono::high_resolution_clock::now();
	for (int i = 0; i < 1000; i++)
		fib_dc(n);
	auto end = chrono::high_resolution_clock::now();
	duration = end - start;
	cout << "- Divide & Conquer took: " << duration.count()/1000 << " seconds" << endl;

	duration = chrono::duration<double>::zero();
	start = chrono::high_resolution_clock::now();
	for (int i = 0; i < 1000; i++)
		fib_mem(n);
	end = chrono::high_resolution_clock::now();
	duration = end - start;
	cout << "- Memoization took: " << duration.count()/1000 << " seconds" << endl;

	duration = chrono::duration<double>::zero();
	start = chrono::high_resolution_clock::now();
	for (int i = 0; i < 1000; i++)
		fib_tab(n);
	end = chrono::high_resolution_clock::now();
	duration = end - start;
	cout << "- Tabulation took: " << duration.count()/1000 << " seconds" << endl;
}


int main()
{
	Fibonacci myFib;
	
	int result1 = myFib.fib_dc(6);
	int result2 = myFib.fib_mem(6);
	int result3 = myFib.fib_tab(6);

	printf("Results for calculating the 6th fibonacci number:\n"
		"- DC: %d, Memoization: %d, Tabulation: %d\n\n",
		result1, result2, result3);

	cout << "Test speed of each implementation with n = 20:\n";
	myFib.timeit(20);

	return 0;
}
