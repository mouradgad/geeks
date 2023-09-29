#include <iostream>
#include <string>

using namespace std;

int main(){

    string S ="bdcauefoh";

    string str;
        char res;
        for(int i=0;i<S.length();i++)
        {
            if(islower(S[i]))
            {
                res = 'z' - S[i]+'a';
                str.push_back(res);
            }
            
            else if(isupper(S[i]))
            {
                res = 'Z' - S[i]+'A';
                str.push_back(res);
            }
            else 
                str += " ";
        }
        cout<<str;
}