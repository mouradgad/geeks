#include <iostream>

using namespace std;

int main (){
    const int mod = 1e9+7;
    int a[]={1,2,3,4,5,6};
    int n =6;
    sort (a,a+n);
    long long int i=0;
    for (long long int j=0 ;j <n;j++){
        i+= (j*a[j]);
    }
    cout<<i%mod ;
}