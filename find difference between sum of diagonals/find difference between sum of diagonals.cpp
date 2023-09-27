#include <iostream>

using namespace std;

int main(){
        int main = 0;
        int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
        int secondary=0;
        int b=Grid.size();

        for (int i=0;i<b;i++){
            main += Grid [i][i];
            secondary +=Grid[i][b-i-1];
        }
            
        int difference = abs(main - secondary);
        cout<<difference;
    
}