class Solution{
public:
    int kthDigit(int A,int B,int K){
        return long(pow(A,B)/pow( 10,--K))% 10;
    }
};