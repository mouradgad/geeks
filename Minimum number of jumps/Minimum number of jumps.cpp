#include <iostream>
using namespace std;
class Solution{
  public:
    int minJumps(int arr[], int n){
        // Your code here
        int jumps =0;
        int currmax =0;
        int maxpos =0;
        for(int i=0;i<n;i++){
            if(i > maxpos){
                return -1;
                
            }
            if(maxpos >= n-1){
                return jumps;
            }
            if(currmax < i+arr[i]){
                currmax  = i+arr[i];
            }
            if(i == maxpos){
                maxpos = currmax;
                jumps++;
            }
        }
        
    }
};