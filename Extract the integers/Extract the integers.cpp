#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    string s="j2x892d3g3eheh8923he";
    vector<string> ans;
    string temp = "";
    
    for(int i = 0; i < s.length(); i++)
    {
        char x = s[i];
        if(x >= '0' && x <= '9')
        {
            temp = temp + s[i];
            if(!isdigit(s[i+1]))
            {
                ans.push_back(temp);
                temp = "";
            }
        }
    }
    cout<<ans;

}