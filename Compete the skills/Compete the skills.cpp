#include <iostream>
using namespace std;

class Solution {
public:
    void scores(int a[], int b[], int &ca, int &cb) {
        for (int i = 0; i < 3; i++) {
            if (a[i] > b[i]) {
                ca++;
            } else if (a[i] < b[i]) {
                cb++;
            }
        }
    }
};

int main() {
    Solution d;
    int a[] = {1, 2, 3};
    int b[] = {2, 1, 5};
    int ca = 0;
    int cb = 0;
    
    d.scores(a, b, ca, cb); // Call the function to update ca and cb
    
    cout << "ca: " << ca << endl;
    cout << "cb: " << cb << endl;

}
