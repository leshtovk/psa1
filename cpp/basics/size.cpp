#include <iostream>
#include <string>

int main(){

    int a = 1000000;
    std::string s = "The hungry rabbit jumps";
    std::string t = "Whatuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuup!";

    int size_a = sizeof(a);
    int size_s = sizeof(s);
    int size_t = sizeof(t);

    std::cout << "Size of a: " << size_a << std::endl;
    std::cout << "Size of s: " << size_s << std::endl;
    std::cout << "Size of t: " << size_t << std::endl;

    return 0;
}
