#include <iostream>
#include <vector>

int main(){
	
	// floats
	// float r = 1.1e15;
	// std::cout << r / 1.e16 << std::endl;
	
	// doubles
	// double a = 0.1;
	// 
	// for (int i = 1; i < 10; ++i) {
	// 	a = a + 0.1;
	// }
	// 
	// std::cout << a << std::endl;
	
	// Rounding
	// double a = 1.342358559999;
	// int aa = static_cast<int>(a);
	// std::cout << a << " rounds to " << aa <<std::endl;
	
	// bools
	// int a = 1;
	// bool nonzero = a != 0;
	// while (nonzero) {
	// 	std::cout << "You lame" << std::endl;
	// 	
	// 	std::cin >> a;
	// 	nonzero = a != 0;
	// }
	
	// lists
	// we get lists with a fixed length are from the `array` library
	// we get lists of variable length from the `vector` library
	// std::vector<int> a({1, 2, 3});
	// int i; // med 0 in 2
	// int ai;
	// 
	// std::cout << "At index 1: " << a[1] << std::endl;
	// std::cout << "At index 0: " << a[0] << std::endl;
	// 
	// std::cout << "Enter which index you would like to change: ";
	// std::cin >> i;
	// std::cout << "Enter the new value at index " << i << ": ";
	// std::cin >> ai;
	// 
	// a[i] = ai;
	// std::cout << "Successfully changed the element at index " << i << " to " << ai << std::endl;
	
	// iteratorji
	std::vector<int> a({12, 4, 5, -2, 11});
	std::vector<int>::iterator it = a.begin();
	std::cout << "The first element of the list is " << *it << std::endl;
	
	++it;
	std::cout << "The second element if the list is " << *it << std::endl;
	
	std::cout << "We are currently at index " << it - a.begin() << std::endl;
	
	int la = a.end() - a.begin();
	std::cout << "The length of the list is " << la << std::endl;
	
	++it;
	std::cout << "The remaining elements of the list are ";
	for (std::vector<int>::iterator itr = it; itr < a.end(); ++itr){
		if (itr + 1 == a.end()){
			std::cout << "and " << *itr;
		}
		else {
			std::cout << *itr << ", ";
		}
	}
	std::cout << std::endl;
	
	
	return 0;
}