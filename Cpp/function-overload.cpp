#include <iostream>

using namespace std;

float timetwo(float num);
int timetwo(int num);

int main() {
	float num1 = 2.4;
	int num2 = 3;

	num1 = timetwo(num1);

	// Set flag
	cout.setf(ios::right);
	// Set the width of cout
	cout.width(4);
	cout << num1 << endl;

	// width must be called for every cout
	cout.width(4);
	num2 = timetwo(num2);
	cout << num2 << endl;

	return 0;
}

float timetwo(float num) {
	return num*2;
}

int timetwo(int num) {
	return num*2;
}
