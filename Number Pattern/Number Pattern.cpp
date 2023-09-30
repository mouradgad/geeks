#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){

vector<string> arr;
for(int i=1;i<N+1;i++){
    string p="";
    for(int j=1;j<i+1;j++){
        p+=to_string(j);
    }
    for(int l=i-1;l>0;l--){
        p+=to_string(l);
    }
    arr.push_back((p));
    
    
}
cout<<arr;
}