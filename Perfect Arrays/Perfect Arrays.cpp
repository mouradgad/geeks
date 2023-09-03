#include <iostream>
#include <string> 
using namespace std;

class Solution{
    public:
    bool IsPerfect(int a[],int n)
    {
     int l=0;
     int d=0;
     for (int i=0 ;i<n;i++){
         if (a[i]==a[n-1-i]){
             l++;
         }
         else{
             d++;
         }
         
     }
     if (d>l){
         return false;
         
     }
     else{
         return true;
     }
    }
};
int main() {
    
    int g = {1,2,3,2,1};
    solution l;
    cout<<l.IsPerfect(g,5);
}