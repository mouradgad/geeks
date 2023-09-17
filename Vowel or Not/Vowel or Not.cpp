#include <iostream>
#include <string>
using namespace std;

int main () {
    string c = "A";
    if(c=="a" || c == "e" || c == "i" || c == "o" || c == "u" || c == "A" || c == "E" || c == "I" || c == "O" || c == "U"){
        cout << "yes";
    }
    else{
        cout<<"no";
    }
}