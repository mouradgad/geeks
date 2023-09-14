#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
class Solution
{
    public:
        bool check (string s)
        {
        	
        	string s2;
        	for(int i=s.length()-1;i>=0;i--){
        	    
        	    s2.push_back(s[i]);
        	   
        	}
        if(s==s2){
            return "true";
        }
        return "false";
        	
        }
};
int main() {
    Solution b;
    string g = "asfsdbavasdfvasdgfasdvg";
    cout<<b.check(g);
}