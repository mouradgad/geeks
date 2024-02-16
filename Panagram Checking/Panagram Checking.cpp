#include <iostream>
using namespace std;

class Solution
{
  public:
    //Function to check if a string is Pangram or not.
    bool checkPangram (string s) {
    int letters[26] = {0};
    for(char c: s)
        if(isalpha(c))
            letters[tolower(c) - 97]++;
    for(int i=0; i<26; i++)
        if(letters[i] < 1)
            return false;
    return true;        
    }

};