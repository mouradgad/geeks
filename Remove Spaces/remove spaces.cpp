#include <iostream>
#include <string> 
using namespace std;

class solution {
private: 
    string modify(string s) {
        int n = s.size();
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] != ' ') {
                s[j] = s[i];
                j++;
            }
        }
        s.resize(j);
        return s;
    }
};

int main() {
    string s = "hello everyone";
    solution w;
    cout << w.modify(s);
    return 0;
}