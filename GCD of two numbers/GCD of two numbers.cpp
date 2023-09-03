#include <iostream>
#include <string> 
using namespace std;
class Solution
{
	public:
    int gcd(int A, int B) 
	{ 
	    if (B==0)
	        return A;
	     else
	        return gcd(B,A%B);
	      
	} 
};

int main() {
    int a = 2;
    int g = 3;
    Solution l;
    cout<<l.gcd(g,a);
}