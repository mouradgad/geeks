#include <iostream>


using namespace std;

int main() {
        int A = 123;
        int B = 12;
        int f = A + B;
        int g = A * B;
        int m;
        int n;
        if (A > B) {
            m = A;
            n = B;
        }
        else {
            m = B;
            n = A;
        }
        int s = m - n;
        int d = m / n;
        
        cout <<f<<"\n"<<g<<"\n"<<s<<"\n"<<d;
}
