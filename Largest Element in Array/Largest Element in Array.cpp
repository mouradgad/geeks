#include <iostream>

using namespace std;


int main (){

    int n =6;
    int arr[]={1,2,3,4,5,6};
    sort(arr.begin(),arr.end());
    cout<<arr[n-1];
}