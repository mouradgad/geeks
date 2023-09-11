#include <iostream>

using namespace std;

int main() {
    int N = 123;
    int sum ;
    for( sum =0; N!=0;N=N/10){
        sum +=N%10;
        
    }
    cout<<sum;
}