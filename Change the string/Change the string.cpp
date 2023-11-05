class Solution{
    public:
    
string modify (string s)
    {
        // your code here
        if(isupper(s[0])){
            for(int i=0;i<s.length();i++){
                s[i]=toupper(s[i]);
            }
            return s;
        }
        else{
              for(int i=0;i<s.length();i++){
                s[i]=tolower(s[i]);
            }
            return s;
        }
    }
};