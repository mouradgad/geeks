class Solution
{
	public:
		int count_divisors(int n)
		{
    int c=0;
    
    for(int a=1; a*a<=n; a++){
        if(n%a==0){
            if(a==n/a){
                if(a%3==0)
                    c++;
            }else{
                if(a%3==0){
                    c++;
                }
                if((n/a)%3==0)
                    c++;
            }
        }
    }
    return c;
		}
};