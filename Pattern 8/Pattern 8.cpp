class Solution{
public:
	
	void printTriangle(int n) {
	    int x=n;
        for(int r=1;r<=n;r++){
            for(int sp=1;sp<=r-1;sp++)
                cout<<" ";
            for(int st=1;st<=2*x-1;st++)
                cout<<"*";
           x=x-1;
           cout<<"\n";
        }
	}
};