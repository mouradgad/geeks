#include <iostream>

using namespace std;

int main (){

    int a[]={1,2,3,4,5,6,7};
    int n=7;

    if(n>=3)
    {
        sort(a,a+n);
        cout<<(a[n-3]);
    }
    cout<<-1;

}