#include <iostream>

template <class T>
T sum(T x1, T x2){

    T result;
    result = x1 + x2;
    return result;
}

int main(){

    int a, b;
    std::cout << "Enter two integers: ";
    std::cin >> a >> b;
    std::cout << sum<int>(a, b) << std::endl;

    double x, y;
    std::cout << "Enter two floating-point numbers: ";
    std::cin >> x >> y;
    std::cout << sum<double>(x, y) << std::endl;

    return 0;
}
