#include<iostream>
#include<vector>

int main() {
	
	std::vector<int> a({1, 2, 3});
	a[2] = 1000;
	
	std::cout << "The elements of the list are: ";
	for (std::vector<int>::iterator it = a.begin(); 
		it < a.end(); ++it) {
			if (it + 1 == a.end()) {
				std::cout << *it << std::endl;
			}
			else {
				std::cout << *it << ", ";
			}
			
		} 
		
	std::cout << "The length of the list is " 
	<< a.end() - a.begin() << std::endl;
	
	return 0;
}