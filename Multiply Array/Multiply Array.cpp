#include <iostream>
using namespace std;

int main(){
    int n = 5;
    int arr[]={1,2,3,4,5};
    int g = 1;
    for(int i=0;i<n;i++){
        g *=arr[i];
    }
    cout<<g;


}