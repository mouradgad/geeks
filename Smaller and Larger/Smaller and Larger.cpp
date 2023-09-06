#include <iostream>

using namespace std;

int main() {
    int x = 3 ; 
    int greater = 0;
    int less = 0 ;
    int arr[] = {23,152,12412,123};
    int n = 4;

    for (int i=0;i<n;i++){
        if (arr[i] >= x){
            greater+=1;
        }
        if(arr[i] <= x){
            less +=1 ; 
            
    }
    }
    cout<<less<<" "<<greater;
    
    }
