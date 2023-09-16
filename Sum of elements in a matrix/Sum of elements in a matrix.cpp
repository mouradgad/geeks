#include <iostream>
using namespace std;

class Solution {
public:
    int sumOfMatrix(int N, int M, int Grid[][2]) {
        int g = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                g += Grid[i][j];
            }
        }
        return g;
    }
};

int main() {
    Solution f;
    int n = 2; 
    int m = 2;

    int a[2][2] = {{11, 12}, {21, 22}}; 
    int result = f.sumOfMatrix(n, m, a);
    cout << result ;
}
