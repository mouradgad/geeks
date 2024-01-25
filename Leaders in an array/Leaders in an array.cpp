class Solution{
    //Function to find the leaders in the array.
    public:
    vector<int> leaders(int a[], int n){
    vector<int> ans;
        int left=0,right=0;
        while(left<n)
        {
            if(a[left]>=a[right+1])
            {
                right++;
                if(right==n-1){
                   ans.push_back(a[left]);
                   left++;
                   right=left;
                }
            }
            else{
                left++;
                right=left;
            }
        }
        ans.push_back(a[n-1]);
        return ans;
    }
};