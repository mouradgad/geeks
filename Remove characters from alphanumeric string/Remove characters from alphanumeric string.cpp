#include <iostream>
#include <string>
using namespace std;


int main(){
        string S ="id891jd8h1hd912hc";
        string d;
	    for (int i =0 ; i<S.length();i++){
	       if(S[i]>='0'&&S[i]<='9'){
	           d += S[i];
	       }
	   }
	   cout<<d;

}