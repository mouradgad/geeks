#include <iostream>
#include <string>

using namespace std;

int main(){
int upper =0;
int lower = 0;
int numbers = 0;
int special = 0;


for (int i=0 ; i<s.length();i++){
    if (s[i] >= 'A' && s[i] <= 'Z'){
        upper++;
    }
    else if(s[i] >= 'a' && s[i] <= 'z'){
        lower++;
    }
    else if (s[i] >= '0' && s[i] <= '9'){
        numbers++;
    }
    else {
        special++;
    }
}
cout<<upper<<lower<<numbers<<special;


}