#include <iostream>

using namespace std;

int main (){

    int n =51;
    while(n >= 2) {
            if(n % 2 != 0) cout<<"false";
            n = n / 2;
        }
        if(n == 1) cout<<"true";
        cout<<"false";
}