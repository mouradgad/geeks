#include <iostream>
#include <string>
using namespace std;
class Solution {
  public:
    string toLower(string S) {
    int n = S.length();
    for (int i = 0 ; i<n ; i++){
            S[i]=tolower(S[i]);
        }
        return S;
    
    }
};
int main() {
string f = " HwUjnaW";
 solution j;
 cout <<j.toLower(f);
}

