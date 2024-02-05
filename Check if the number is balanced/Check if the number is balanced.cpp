class Solution{
public:	
    bool balancedNumber(string s)
    {
        int n=s.size();
        int mid=n/2;
        long long int s1=0,s2=0;
        for(int i=0;i<mid;i++)
        {
            s1+=(s[i]-'0');
        }
        for(int i=mid+1;i<n;i++)
        {
            s2+=(s[i]-'0');
        }
        return(s1==s2);
 
    }
};