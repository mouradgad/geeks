class Solution {
  public:
    int getCompundInterest(int P, int T , int N , int R) {
        return P*pow((1+(R/100.0)/N),N*T);
    }
};