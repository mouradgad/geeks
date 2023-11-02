#include <iostream>
#include <string>
class Solution{
    public:
    bool isSubSequence(string A, string B) 
    {
        int l=0;
        for(int i=0;i<B.size();i++){
            if(B[i]==A[l]){
                l++;}
        }
        if(l==A.size()){
            return true;}
            
        else {
            return false;}
            
    }
    
};