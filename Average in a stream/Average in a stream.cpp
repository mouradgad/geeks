#include <iostream>
#include <string>
#include <vector> 

using namespace std;

int main() {
    float sum=0;
    vector<float> ans;
    for(int i=0;i<n;i++)
    {
        sum+=arr[i];
        ans.push_back(sum/(i+1));
    }
    return ans;
}