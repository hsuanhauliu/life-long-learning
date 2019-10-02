#include <iostream>

using namespace std;

struct Node {
	int value;
	Node(int input) {
		value = input;
	}
};

typedef struct Node Node_t;

int main() {
	// Point at static variable.
	int test1 = 1;
	int* pointer1 = &test1; // copy the address of test1 to the pointer
	cout << "Static variable:"<< *pointer1 << endl << endl;

	// Point at dynamic object.
	int* pointer2 = new int(2); // dynamically create an int object
	cout << "Dynamic object: " << *pointer2 << endl; // print the object that it's pointing to
	cout << "Object address: " << pointer2 << endl << endl; // print the address that is stored in the pointer

	// Point at a struct object.
	Node* point3 = new Node(3);
	cout << "Dynamic struct: " << point3->value << endl;


	return 0;
}
