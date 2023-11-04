class Solution{
  public:
    int missingNumber(vector<int>& array, int n) {
        int i=1;
        int sum =0,sum1=0;
        sum1=(n*(n+1))/2;
        sum=array[0];
        while(i<n-1){
            sum+=array[i++];
        }
        
        return sum1-sum;
    }
};