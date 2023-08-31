#include <iostream>
using namespace std;
class Solution {
  public:
    int nthTermOfAP(int A1, int A2, int N) {
        int answer = A1+(N-1)*(A2-A1);
        return answer;
    }
};
int main() {
    int w=2;
    int r=3;
    int N=4;
    Solution e;
    cout<<e.nthTermOfAP(w,r,N);
}