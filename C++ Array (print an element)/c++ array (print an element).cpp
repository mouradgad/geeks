#include <iostream>
using namespace std;

class solution {
public:
    int findElementAtIndex(int a[], int n, int key) {
        return a[key];
    }
};

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    solution s;
    cout << s.findElementAtIndex(a, 5, 2);
    return 0;
}