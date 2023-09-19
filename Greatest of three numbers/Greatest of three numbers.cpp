#include <iostream>

using namespace std;

int main(){
    int A = 3;
    int B=9;
    int C = 13;
    if (A >= B and A >= C) {
        cout<<A;
    }
    if (B >= A and B >= C) {
        cout<<B;
    }
    if (C >= A and C >= B) {
        cout<<C;
    }
}