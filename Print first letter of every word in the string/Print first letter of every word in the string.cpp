class Solution{
public:	
	
	string firstAlphabet(string S)
	{
	   string h;
	   h+=S[0];
	   for (int i=0;i<S.length();i++){
	       if(S[i]==' '){
	           h+=S[i+1];
	       }
	   }
	   return h;
	}
};