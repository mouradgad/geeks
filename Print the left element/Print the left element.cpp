#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a[] = {1,2,3,41,2,15,125,15};
    int n = 8;
    sort(a,a+n);
    int mid = (n-1)/2;
    cout<<a[mid];
}