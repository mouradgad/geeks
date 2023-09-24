#include <iostream>
#include <string>
using namespace std;



int main(){
    int N =13;
    int temp=N,last,sum=0;
        while(temp>0){
            int fact=1;
            last=temp%10;
            for(int i=1;i<=last;i++){
                fact=fact*i;
            }
            sum+=fact;
            temp/=10;
        }
        if(sum==N)
            cout<<1;
        else
            cout<<0;
}