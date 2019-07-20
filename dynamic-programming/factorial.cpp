/* Author: Hsuan-Hau Liu
 * File: factorial.cpp
 * Description: A demonstration of dynamic programming implementation of factorial.
 * Note: compile with C++11 enabled. i.e. g++ factorial.cpp -std=c++11
 */

#include <iostream>
#include <chrono>

using namespace std;

#define MAX 50

class Factorial
{
public:
	int fac_dc(int n);
	int fac_mem(int n);
	int fac_tab(int n);
	void timeit(int n);

private:
	int fac_recurrence(int n, int table[]);
};

int Factorial::fac_dc(int n)
{
	if (n == 0)
		return 1;
	return n * fac_dc(n-1);
}

int Factorial::fac_mem(int n)
{
	int table[MAX] = {0};	// table for memoization
	table[0] = 1;
	return fac_recurrence(n, table);
}

// fac_mem helper function
int Factorial::fac_recurrence(int n, int table[])
{
	if (table[n] != 0)
		return table[n];
	table[n] = n * fac_recurrence(n-1, table);
	return table[n];
}

int Factorial::fac_tab(int n)
{
	int table[MAX] = {0};
	table[0] = 1;

	for (int i = 1; i <= n; i++)
		table[i] = i * table[i-1];
	
	return table[n];
}

// Run each function 1000 times and get the average time.
void Factorial::timeit(int n)
{
	auto start = chrono::high_resolution_clock::now();
	for (int i = 0; i < 1000; i++)
		fac_dc(n);
	auto end = chrono::high_resolution_clock::now();
	chrono::duration<double> duration = end - start;
	cout << "- Divide & Conquer took: " << duration.count()/1000 << " seconds" << endl;

	duration = chrono::duration<double>::zero();
	start = chrono::high_resolution_clock::now();
	for (int i = 0; i < 1000; i++)
		fac_mem(n);
	end = chrono::high_resolution_clock::now();
	duration = end - start;
	cout << "- Memoization took: " << duration.count()/1000 << " seconds" << endl;

	duration = chrono::duration<double>::zero();
	start = chrono::high_resolution_clock::now();
	for (int i = 0; i < 1000; i++)
		fac_tab(n);
	end = chrono::high_resolution_clock::now();
	duration = end - start;
	cout << "- Tabulation took: " << duration.count()/1000 << " seconds" << endl;
}

int main()
{
	Factorial myFac;

	int result1 = myFac.fac_dc(6);
	int result2 = myFac.fac_mem(6);
	int result3 = myFac.fac_tab(6);
	printf("Results for calculating factorial of 6:\n"
		"- DC: %d, Memoization: %d, Tabulation: %d\n\n",
		result1, result2, result3);

	cout << "Test speed of each implementation with n = 20:\n";
	myFac.timeit(20);

	return 0;
}
