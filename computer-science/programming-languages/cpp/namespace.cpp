#include <iostream>

using namespace std;

namespace name1 {
	void hello();
}

namespace name2 {
	void hello();
}

int main() {
	// I can call two functions that have the same exact name from different namespaces.
	name1::hello();
	name2::hello();

	return 0;
}

namespace name1 {
	void hello() {
		cout << "Hello from namespace 1!" << endl;
	}
}

namespace name2 {
	void hello() {
		cout << "Hello from namespace 2!" << endl;
	}
}
