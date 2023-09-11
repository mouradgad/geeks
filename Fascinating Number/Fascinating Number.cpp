#include <iostream>
#include <string>
#include <algorithm> 
using namespace std;

int main() {
    int n = 42; 
    string s = to_string(n * 2);
    string e = to_string(n * 3);
    string q = to_string(n);
    string v = s + e + q;
    string h = "123456789"; 

    sort(v.begin(), v.end());

    if (h == v) {
        cout << "yes";
    } else {
        cout << "no";
    }
}