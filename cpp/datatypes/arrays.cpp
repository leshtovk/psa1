#include <iostream>

int main(){

    int foo [5];
    std::cout << "`foo` has been initialized to " << foo << " \n..." << std::endl;
    std::cout << "the size of `foo` is initialized to " << sizeof(foo) << std::endl;

    int boo[] = {1, 2, 4, 1};
    int sum_boo = 0;
    for (int i = 0; i < 4; i++){
        sum_boo += boo[i];
    }
    std::cout << "sum of the elements of `boo`: " <<sum_boo << std::endl;

    return 0;
}
