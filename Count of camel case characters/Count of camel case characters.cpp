#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution
{
  public:   
    int countCamelCase (string s)
    {
        int count = 0;
        for (int i=0 ; i<s.length();i++){
            if(s[i]>='A' && s[i]<='Z' ){
                count++;
            }
        }
        return count;
    }
};

int main() {
    Solution d;
    string s = "asifnhsdivnasinefOANSOIFA";
    cout<<d.countCamelCase(s);
}