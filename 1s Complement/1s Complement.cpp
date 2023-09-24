#include <iostream>
#include <string>
using namespace std;

int main(){
    string S = "101";
    string d = "";
        for (int i =0 ;i<S.length();i++){
            if (S[i]=='0'){
                d+='1';
                
            }
            else{
                d+='0';
            }
        }
        cout<<d;
}