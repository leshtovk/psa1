#include <iostream>
#include <string>

int main(){

    char inp[20];
    std::cin >> inp;
    std::cout << "You entered the C-style string: " << inp << std::endl;
    std::cout << "Its length is " << (sizeof(inp) / sizeof(*inp)) << std::endl;

    return 0;
}
