#include <iostream>

int main() {
	
	// define an enumeration called `Color`
	enum Color { RED, YELLOW, GREEN };
	Color c = RED;
	
	switch (c) {
		case YELLOW: 
			std::cout << "It's yellow\n"; break;
		case RED: 
			std::cout << "It's red\n"; break;
		case GREEN:
			std::cout << "It's green\n"; break;
	}
	
	return 0;
}