#include <iostream>

int main(){
	
	int s;
	
	std::cout << "Enter a number: ";
	std::cin >> s;
	
	while(s != 0){
		
		for (int i = 1; i*i < s; ++i){	
			if (i % 2 != 0){
				std::cout << i*i;
			} else {
				std::cout << "		" << i*i << std::endl;
			}
		}
		
		std::cout << std::endl;
		std::cout << "Enter a number: ";
		std::cin >> s;
	
	}
	
	return 0;
	
}