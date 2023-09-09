#include <iostream>

using namespace std;

int main() {
        int d = 1;
        int n = 14;
        int r = 5;
        for (int i = 1; i <= n; ++i) {
            d *= i;
        }

        for (int i = 1; i <= n - r; ++i) {
            d /= i;}
            
        cout<<d;
}