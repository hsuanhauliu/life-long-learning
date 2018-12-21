#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

// prototypes
long long int factorial(int num);
void quicksort(vector<int> &nums, int start, int end);
int partition(vector<int> &nums, int start, int end);

int main() {
	// First example
	int input;
	cout << "----------Example 1: Factorial----------\n";
	cout << "Enter a small positive integer: ";
	cin >> input;
	long long int fac = factorial(input);
	cout << "The factorial of the input number is: " << fac << endl << endl;
	
	// Second example
	cout << "----------Example 2: Quick Sort----------\n";
	vector<int> inputs;
	srand(time(0)); // make the numbers random
	for (int i = 0; i < 10; i++)
		inputs.push_back(rand() % 100); // randomly produce a number between 0~99
	cout << "Original array: ";
	for (int i = 0; i < 10; i++)
		cout << inputs[i] << " ";
	cout << endl;

	quicksort(inputs, 0, inputs.size() - 1);

	cout << "After sorting:  ";
	for (int i = 0; i < 10; i++)
		cout << inputs[i] << " ";
	cout << endl << endl;

	return 0;
}

// Use recursion to calculate factorial
long long int factorial(int num) {
	long long int sum = num;

	// base case
	if (num == 0)
		return 0; // factorial of 0 is 1
	else if (num == 1)
		return 1; // return 1 when it reaches 1
	else
		sum *= factorial(--num); // decrement by one then pass it into the function

	return sum;
}

// Recursive quick sort
void quicksort(vector<int> &nums, int start, int end) {
	if (start < end) {
		int pivot = partition(nums, start, end);
		quicksort(nums, start, pivot - 1);
		quicksort(nums, pivot + 1, end);
	}
}

// Partition function for quick sort
int partition(vector<int> &nums, int start, int end) {
	int pivot = nums[end]; // use the last element as pivot 
	int curr = start; // index of the element to be swapped

	// start checking from the beginning
	for (int i = start; i < end; i++) {
		if (nums[i] < pivot) {
			int temp = nums[curr];
			nums[curr++] = nums[i];
			nums[i] = temp;
		}
	}

	// move the pivot to its correct place
	int temp = nums[curr];
	nums[curr] = nums[end];
	nums[end] = temp;

	return curr;
}
