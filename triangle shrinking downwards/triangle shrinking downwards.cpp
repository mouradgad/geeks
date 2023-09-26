#include <iostream>
using namespace std;


int main(){
    string S="isoianno";
    string str="";
        
        for(int i=0;i<S.size();i++)
        {
            for(int j=0;j<i;j++)
            {
                str+=".";
            }
            for(int j=i;j<S.size();j++)
            {
                str+=S[j];
            }
        }
        cout<<str;
}