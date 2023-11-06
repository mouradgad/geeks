class Solution {
  public:
    void printTriangle(int n) {
            int a=0;
       for(int i=1;i<=n;i++)
       {
           for(int k=1;k<=(n-i);k++)
           {
               cout<<" ";
           }
           for(int j=1;j<=(i+a);j++)
           {
               cout<<"*";
           }
           a++;
           cout<<endl;
       }
    }
};