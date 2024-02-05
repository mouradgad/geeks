class Solution{
public:
	
	int countSubstr (string S)
	{
	  int ans=0;
        int temp=0;
        for(int i=0;i<S.length();i++)
        {
            if(S[i]=='1')
            {
                ans+=temp;
                temp++;
            }
        }
        return ans;  
	}
};