#include <iostream>


using namespace std;


int main(){
    int N = 5;
    int A[]={1,2,3,4,5};
    int f=0;
    for (int i = 0 ; i<N; i++){
        f += A[i];
    }
    f = f/N;
    return f;
}