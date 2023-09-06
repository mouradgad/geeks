#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int a[] = {1, 2, 3, 4, 6, 51, 5};
    int n = 7;
    sort(a, a + n);

    vector<int> ans;
    for (int i = 0; i < n - 2; i++) {
        ans.push_back(a[i]);
    }

    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }

    return 0;
}
