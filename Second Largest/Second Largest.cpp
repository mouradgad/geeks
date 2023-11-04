class Solution{
public:	
	// Function returns the second
	// largest elements
	int print2largest(int arr[], int n) {
	   sort(arr,arr+n);
       int secondlargest=0;
       for(int i=n-1;i>=0;i--)
       {
           if(arr[i]!=arr[i-1])
           {
               secondlargest=arr[i-1];
               break;
           }
       }
       if(secondlargest==0)
       {
           return -1;
       }
       return secondlargest;
    }
	
};