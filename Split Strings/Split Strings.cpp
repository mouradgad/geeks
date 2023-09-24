#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(){
    string S = "nsd9ch189dh1nwon189ndc!!@#";
    vector<string> ans;
        string temp1,temp2,temp3;
        for(int i=0;i<S.length();i++){
            if(isalpha(S[i])){
                temp1.push_back(S[i]);
            }
            else if(isdigit(S[i])){
                temp2.push_back(S[i]);
            }
            else{
                temp3.push_back(S[i]);
            }
        }
        ans.push_back(temp1);
        ans.push_back(temp2);
        ans.push_back(temp3);
        cout<<ans;
}