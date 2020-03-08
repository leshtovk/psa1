#include <iostream>
#include <vector>
#include <math.h> 	/* sqrt */

// checks whether a number is perfect
bool popolno(long long int n){
	long long int divisor_sum = 0;
	long long int bound = static_cast<long long int>(n / 2);
	for (long long int i = 1; i <= bound + 1; ++i) {
		// `bound + 1` just to be sure  
		if (n % i == 0){
			std::cout << i << " is a divisor\n";
			divisor_sum += i;
		}
	}
	std::cout << "divisor sum: " << divisor_sum << std::endl;
	return divisor_sum == n;
}

// // returns a vector of the first `n` perfect numbers
// // see all known perfect numbers before using this 
// // make sure to make the necessary changes to `popolno`
// std::vector<int> popolna(int n) {
// 	std::vector<int> x(n);
// 	int count = 0;
// 	int i = 2;
// 	while (count < n) {
// 		if (popolno(i)){
// 			x[count] = i;
// 			++count;
// 		}
// 		++i;
// 	}
// 	return x;
// }

void preveri_popolnost(long long int n){
	if (popolno(n)) {
		std::cout << n << " is a perfect number!\n";
	}
	else {
		std::cout << n << " is not a perfect number!\n";
	}
	
}

int main() {
	
	// long long int n = 8589869056;
	// // std::cout << "Enter a number: ";
	// // std::cin >> n; 
	// preveri_popolnost(n);
	
	// // see list of known perfect numbers before running this section 
	// int n;
	// std::cout << "Enter a number: ";
	// std::cin >> n;
	// std::vector<int> c = popolna(n);
	// 
	// std::cout<< "The first " << n << " perfect numbers: ";
	// for (std::vector<int>::iterator it = c.begin(); 
	// 	it < c.end(); ++it){
	// 		if (it + 1 == c.end()) {
	// 			std::cout << *it << std::endl;
	// 		}
	// 		else{
	// 			std::cout << *it << ", ";
	// 		}
	// 	}
	
	return 0;
}