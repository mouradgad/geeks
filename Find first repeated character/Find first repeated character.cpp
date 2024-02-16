#include <iostream>
using namespace std;

class Solution:

    string firstRepChar(string s)
{
    unordered_map<char,int>mp;
    
    
      for (int i = 0; i < s.size(); i++)
    {
         mp[s[i]]++;
        if(mp[s[i]]>1){
        return string(1,s[i]);
        break;
        }
    }
    return "-1";
    
}