#include <iostream>
using namespace std;

int main(){
    int matrix = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };
    int sum =0;
    for (int i =0 ; i<matrix.size();i++){
            sum+= matrix[i][i]+ matrix[i][matrix.size()-1-i];
            
    
    }
    cout<<sum;
}