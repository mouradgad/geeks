#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N; 

    if (N == 1) {
        cout << "one";
    }
    else if (N == 2) {
        cout << "two";
    }
    else if (N == 3) {
        cout << "three";
    }
    else if (N == 4) {
        cout << "four";
    }
    else if (N == 5) {
        cout << "five";
    }
    else if (N == 6) {
        cout << "six";
    }
    else if (N == 7) {
        cout << "seven";
    }
    else if (N == 8) {
        cout << "eight";
    }
    else if (N == 9) {
        cout << "nine";
    }
    else if (N == 10) {
        cout << "ten";
    }
    else if (N > 10 || N < 1) {
        cout << "not in range";
    }

}
