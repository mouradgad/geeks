#include <iostream>
#include <string>

using namespace std;

int main() {

    int n = 10;
    char arr[]="e r s g zv";

    string s = "";
    for (int i = 0; i < n; i++) {
        if (arr[i] != ' ') {
            s += arr[i];
        }
    }

    cout << s ;
}
