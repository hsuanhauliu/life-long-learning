#include <iostream>
#define tab '\t'

using namespace std;

struct data {
	string name;
	int age;
	float height;
};

// Overloaded insertion operator for data struct
ostream& operator << (ostream& str_out, struct data& d) {
	str_out << d.name << tab;
	str_out << d.age << tab;
	str_out << d.height << endl;
	return str_out;
}

class info {
public:
	string name;
	int age;
	float height;
};

// Overloaded insertion operator for info class
ostream& operator << (ostream& str_out, class info& i) {
	str_out << i.name << tab;
	str_out << i.age << tab;
	str_out << i.height << endl;
	return str_out;
}

int main() {
	struct data person1 = {"Stuart Snaith", 21, 2.01};
	struct data person2 = {"Kevin Keegan", 42, 1.56};
	struct data person3 = {"Mein Gott", 12000, 0.99};

	class info info1 = {"Anna", 20, 1.44};
	class info info2 = {"Andrew", 31, 1.80};
	class info info3 = {"Andy", 50, 1.62};

	cout << person1;
	cout << person2;
	cout << person3 << endl;

	cout << info1;
	cout << info2;
	cout << info3;

	return 0;
}
