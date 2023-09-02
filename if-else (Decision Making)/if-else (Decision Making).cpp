#include <iostream>
using namespace std;
class Solution {
  public:
     string compareNM(int n, int m){
        if (n > m)
        return "greater";
        else if(n ==m)
        return "equal";
        else
        return "lesser";
     }
};
int main() {
    int w=2;
    int r=3;
    Solution e;
    cout<<e.compareNM(r,w);
}