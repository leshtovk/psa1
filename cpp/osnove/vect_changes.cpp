#include<iostream>
#include<vector>
#include<numeric>	// for 'iota'

int main() {
	
	std::vector<int> x(1000);	// a vector of 1000 zeros
	std::iota(std::begin(x), std::end(x), 1);
		// similar to `range()` in python
		// the first two arguments are iterators that point to
		// our chosen initial and final positions of the vector 
		// the last argument is the starting number
	
	x.pop_back();
	x.push_back(1000000);
	
	// try not to use:
	// iterator erase(iterator pos)
	// iterator insert(iterator pos, T vrednost)
	
	for (std::vector<int>::iterator it = x.begin();
		it < x.end(); ++it) {
			std::cout << *it << " ";
		}
	std::cout << std::endl;
	
	
	
	
	return 0;
}