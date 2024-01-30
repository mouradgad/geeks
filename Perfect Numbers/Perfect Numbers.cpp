class Solution {
  public:
    int isPerfectNumber(long long N) {
        if(N==1)
        return false;
        long long int sum=0;
        for(int i=0;i<N;i++){
            sum+=i;
            if(sum>N){
                return 0;
            }
            if(sum==N)
            return 1;
        }
    }
};