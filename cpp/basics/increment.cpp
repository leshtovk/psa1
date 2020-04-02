#include <iostream>

int main(){

    int x = 3;
    int y = ++x;

    int z = 3;
    int w = z++;

    std::cout << "x contains " << x << ", y contains " << y << std::endl;
    std::cout << "z contains " << z << ", w contains " << w << std::endl;

    return 0;
}
