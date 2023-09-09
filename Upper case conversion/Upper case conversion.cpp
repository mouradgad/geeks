#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "hi every one" ;string s1; int i;
   s1.push_back(toupper(s[0]));
   for(int i=1;i<s.size();i++)
  {
      if(s[i-1]==' ')
      {
      s1.push_back(toupper(s[i]));
      }
      else
      s1.push_back(s[i]);
  }
   cout<<s1;
}