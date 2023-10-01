#include <iostream>

using namespace std;

int main(){
    string str="owuhoashah";
    string f = "";
    
    int n = str.length();
    
    for(int i=n-1;i>=0;i--){
        
        f += str[i];
    }
    cout<<f;
}