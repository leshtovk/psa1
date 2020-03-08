#include <iostream>
#include <vector>
#include <numeric> // for `iota`
#include <string>
#include <set>
#include <unordered_set>
#include <map>

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
	
	// ----------------------------------------------------------
	
	// bools
	
	// int a = 1;
	// bool nonzero = a != 0;
	// while (nonzero) {
	//     std::cout << "You lame" << std::endl;
	//     	
	//     std::cin >> a;
	//     nonzero = a != 0;
	// }
	
	// ----------------------------------------------------------
	
	// vectors

	// std::vector<int> a({1, 2, 3});
		// a list with a fixed length is an `array`
		// a list of variable length is a`vector`
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
	
	// ----------------------------------------------------------
	
	// iterators
	
	// std::vector<int> a({12, 4, 5, -2, 11});
	// std::vector<int>::iterator it = a.begin();
	// std::cout << "The first element of the list is " << *it << std::endl;
	// 
	// ++it;
	// std::cout << "The second element if the list is " << *it << std::endl;
	// 
	// std::cout << "We are currently at index " << it - a.begin() << std::endl;
	// 
	// int la = a.end() - a.begin();
	// std::cout << "The length of the list is " << la << std::endl;
	// 
	// ++it;
	// std::cout << "The remaining elements of the list are ";
	// for (std::vector<int>::iterator itr = it; itr < a.end(); ++itr){
	// 	if (itr + 1 == a.end()){
	// 		std::cout << "and " << *itr;
	// 	}
	// 	else {
	// 		std::cout << *itr << ", ";
	// 	}
	// }
	// std::cout << std::endl;
	
	// std::vector<int> b(100);
	// for (std::vector<int>::iterator it = b.begin();
	// 	it < b.end(); ++it) {
	// 		std::cout << it - b.begin() + 1 
	// 		<< ": " << *it << std::endl; 
	// 	}
	
	// ----------------------------------------------------------
	
	// changing vectors 
	
	std::vector<int> x(1001);	// a vector of 1000 zeros
	std::iota(std::begin(x), std::end(x), -500);
		// similar to `range()` in python, fills the range [m, n)
		// the first two arguments are iterators that point to
		// our chosen initial and final positions of the vector 
		// the last argument is the starting number
	
	x.pop_back();
	x.push_back(5000000);
	
	// try not to use:
	// iterator erase(iterator pos)
	// iterator insert(iterator pos, T vrednost)
	
	for (std::vector<int>::iterator it = x.begin();
		it < x.end(); ++it) {
			std::cout << *it << " ";
		}
	std::cout << "\n\nlength: " << x.size() << std::endl;
	
	// ----------------------------------------------------------
	
	// character strings
	
	// std::string name;
	// std::string delimiter = " ";
	// 
	// std::cout << "Enter thein name: ";
	// std::getline (std::cin, name);
	// 	// get line from input stream
	// 	// store the characters into `str`
	// 	
	// std::string firstname = name.substr(0, name.find(delimiter));
	// std::cout << "Sup " << firstname << std::endl;
	
	// ----------------------------------------------------------
	
	// sets 
	
	// // std::set<typename T>	-- ordered, slower
	// std::set<int> a({1, 2, 2, 2, 1, 5, 6, 7, 8, 123123, 0});
	// 
	// std::cout << "Thein ordered set: {";
	// for (std::set<int>::iterator it = a.begin();
	// 	it != a.end(); ++it) {
	// 		if (std::next(it, 1) == a.end()) {
	// 		std::cout << *it << "}" << std::endl;
	// 		}
	// 		else {
	// 			std::cout << *it << ", ";
	// 		}
	// 	}
	// // note: 
	// // `+` and `-` can't be used on `std::set<int>::iterator` 
	// 	
	// // std::unordered_set<typename T> -- unordered, faster
	// std::unordered_set<int> b({213213, 231, 5, 12343, 0, 8, 32});
	// 
	// std::cout << "Thein unordered set: {";
	// for (std::unordered_set<int>::iterator it = b.begin();
	// 	it != b.end(); ++it) {
	// 		if (std::next(it, 1) == b.end()) {
	// 			std::cout << *it << "}" << std::endl;
	// 		}
	// 		else {
	// 			std::cout << *it << ", "; 
	// 		}
	// 	}
	// 	
	// // keep in mind `a` and `b` are different types of sets
	// int i = 0;
	// std::cout << "The amount of common elements: ";
	// for (std::set<int>::iterator it = a.begin();
	// 	it != a.end(); ++it){
	// 		if (b.find(*it) != b.end()) {
	// 			// `b.end()` returns an iterator referring
	// 			// to the past-the-end element of `b`
	// 			++i;
	// 		}
	// 	}
	// std:: cout << i << std::endl;
		
	// ----------------------------------------------------------

	// maps and pairs
	
	// // std::pair<int, std::string> p = std::make_pair(1, "dude");
	// // std::cout << "(" << p.first << ", " << p.second << ")\n";
	// 
	// std::string chars = "alphabeta";
	// std::map<char, int> counter;
	// 
	// for (int i = 0; i < chars.length(); ++i){
	// 	counter[chars[i]]++;
	// }
	// 
	// // the `std::map<char, int>::iterator` is a pair
	// for (std::map<char, int>::iterator it = counter.begin();
	// 	it != counter.end(); ++it) {
	// 		std::cout << it -> first << " => " << it -> second			 
	// 				  << "  is the same as  " 
	// 				  << (*it).first << " => " << (*it).second
	// 		<< std::endl;
	// 	}
		
	
	return 0;
}