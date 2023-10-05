#include <iostream>
using namespace std;

int main (){
    int a[]={1,2,2,3,4,5};
    k=2;
    n=6;
    for(int i=0;i<n;i++){
        m[a[i]]++;
        if(m[a[i]] >= k){
            cout<<a[i];
        }
    }
    cout<<-1;

}