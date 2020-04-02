#include <iostream>
#include <string>

int main(){

    int x, y;
    std::cout << "Enter two numbers: ";
    std::cin >> x >> y;

    std::string s = (x == y) ? "Equal" : "Not equal";
    std::cout << s << std::endl;

    return 0;
}
