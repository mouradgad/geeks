#include <iostream>

using namespace std;

int main(){
    int N = 4;
    int number = 1;
        for (int i=1;i<=N;i++){
            for (int j=1;j<=i;j++){
                cout<<number<<" ";
                number++;
            }
        cout<<"\n";}
}