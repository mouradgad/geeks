#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
  public:
    int isDigitSumPalindrome(int N) {
        string f =to_string(N);
        int sum=0;
        
        for (char i : f){
            sum += i - '0';
        }
        string g = to_string(sum);
        string h = g;
        reverse(h.begin(),h.end());
        if (g == h){
            return 1;
        }
        else{
            return 0;
        }       
    }
};
int main() {
    int n = 61245;
    Solution p;
    cout<<p.isDigitSumPalindrome(n);
}