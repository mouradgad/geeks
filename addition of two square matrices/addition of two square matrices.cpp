#include <iostream>

using namespace std;

int main (){
    int matrixA={
        {1,2,3},
        {4,5,6}
    };
    int matrixB={
        {1,2,3},
        {4,5,6}
    };
    int n = matrixA.size();
    
        for (int i = 0 ; i<n;i++){
            for (int j=0 ; j<n;j++){
                matrixA[i][j]+=matrixB[i][j];
            }
            }
            cout<<matrixA; 
}