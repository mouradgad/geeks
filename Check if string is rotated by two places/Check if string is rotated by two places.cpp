class Solution
{
    public:
    //Function to check if a string can be obtained by rotating
    //another string by exactly 2 places.
    bool isRotated(string str1, string str2)
    {
        // Your code here
        int n1=str1.size();
        int n2=str2.size();
        if(n1!=n2||n1<2)
        return 0;
        string s="";
        string s1="";
        for(int i=2;i<n1;i++)
        {
            s+=str1[i];
        }
        s+=str1[0];
        s+=str1[1];
        s1+=str1[n1-2];
        s1+=str1[n1-1];
        for(int i=0;i<n1-2;i++)
        {
            s1+=str1[i];
        }
        if(s==str2||s1==str2)
        {
            return 1;
        }
        return 0;
    }

};