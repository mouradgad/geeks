class Solution{
public:	
	
	    int shortestDistance(vector<string> &s, string word1, string word2)
    {
        int first=-1;
        int second=-1,ans=INT_MAX;;
        
        for(int i=0; i<s.size(); i++)
        {
                if(s[i]==word1)
                first=i;
                
                if(s[i]==word2)
                second=i;
                
                if(first!=-1 && second!=-1)
                {
                    ans=min(ans,abs(first-second));
                }
        }
        
        return ans;
    }


};