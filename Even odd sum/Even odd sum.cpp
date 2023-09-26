#include <iostream>

using namespace std;

int main(){
    int Arr[]={1,2,3,4,5,6,7,8}
    int odd = 0;
    int even = 0;
        
        for(int i= 0; i<N;i++){
            if(i%2==0){
                odd += Arr[i];
                
            }
            else{
                even+=Arr[i];
            }
        }cout<<odd<<even;
}