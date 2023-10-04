#include <iostream>

using namespace std;

int main (){
    int N =8;
    if(N == 1) return 0; 
        
        for(int i=2; i*i<=N; i++) {
             if(N%i == 0) {
                cout<<0 ;
             }
        }
        cout<<1;
}
