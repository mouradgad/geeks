class HelloWorld {
    public static int[] reverse(int[] arr){
        int n=arr.length;
        int[] arr1 = new int[n];
        
        for (int i =0;i<=n;i++){
            int biggest = arr[0];
            for (int j = 0 ; j<=n; j++){
                for (int k=0;k<=n;k++){
                    if (biggest<=arr[k]){
                    biggest = arr[k];
                }
                }
                
                arr1[i]=biggest;
                arr[j]=0;
            }
        }
        return arr1;
    }
    public static void main(String[] args) {
        System.out.println("Try programiz.pro");
        int [] array = {21125,32612,62,6126,1};
        System.out.println(reverse(array));
    }
}