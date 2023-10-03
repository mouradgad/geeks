#include <iostream>
#include <vector>

using namespace std;

int main (){

    vector<long long int>ans;
        int n =5;
        int long long n1=0;
        int long long n2=1;
        int long long n3;
        for (int i=0;i<n;i++){
            if (i==1){
                ans.push_back(n2);}
            else{
                n3=n1+n2;
                ans.push_back(n3);
                n1=n2;
                n2=n3;}
        }
        cout<<ans;

}