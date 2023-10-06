#include <iostream> 
#include <string>
using namespace std;

int main (){
    string s1="HI";

    string s2="IH";
    string str = s1+s1;
    int len1=s1.length();
    int len2=s2.length();
    if(len1!=len2){
        cout<<false;}
    if(str.find(s2) != string::npos){
        cout<<true;}
    cout<<false;

}