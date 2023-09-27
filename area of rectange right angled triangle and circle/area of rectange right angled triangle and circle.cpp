#include <iostream>
#include <vector>
using namespace std;

int main(){
    int L=2;
    int W=5;
    int B=3;
    int H=7;
    int R=3;
    int area1=L*W;
    int area2=0.5*B*H;
    int area3=3.14*(R*R);
    vector<int> arr;
    arr.push_back(area1);
    arr.push_back(area2);
    arr.push_back(area3);

    return arr;

}