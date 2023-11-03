class Solution{
public:
    void printTriangle(int n) {
        int stars = 1;
        for( int i = 1 ; i <= (2*n-1); i++){
            for(int j = 1; j <= stars ; j++){
                cout << "* ";
            }
            if( i >= n ) stars--;
            else stars++;
            cout << endl;
        }
    
    }
};