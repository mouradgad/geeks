#include <iostream>

using namespace std;


int main (){
    int N = 4;
    if (N < 0) {
        return 0;
    }
    long long int result = 1;
    for (int i = 2; i <= N; ++i) {
        result *= i;
    }
    cout<<result;

}