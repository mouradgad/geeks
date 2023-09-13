#include <iostream>
#include <string

using namespace std;

int main() {
    string S="asdofaschioasehfs";
    string result;
for (int i = 0; i < S.length(); i++) {
        if (i % 2 == 0) {
            result += S[i];
        }
    }
    cout<<result;
}