#include <iostream>
using namespace std;
class Solution
{
    public:
    //Function to find a continuous sub-array which adds up to a given number.
    vector<int> subarraySum(vector<int>arr, int n, long long s){
        int left=0,right=0;
        
        while(right<n){
            s-=arr[right];
            while(s<0 and left<right){
                s+=arr[left++];
            }
            if(s==0)return {left+1,right+1};
            right++;
        }
        
        return {-1};
    }
};