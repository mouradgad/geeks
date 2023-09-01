#include <iostream>
#include <string>
using namespace std;
class solution{
    public:
    string compareFive(int n){

    if (n>5)
    return "Greater than 5";
    else if (n<5)
    return "Less than 5";
    else
    return "Equal to 5";
    }
};
int main() {
    int n = 6;
    solution p;
    cout<<p.compareFive(n);
}