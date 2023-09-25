#include <iostream>

using namespace std;

int main (){
    int n =6;
    int even = n / 2;
    int odd = n - even;
    int g = odd * odd;
    int b = even * (even + 1);
    return {g,b};
}