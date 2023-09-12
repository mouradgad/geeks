#include <iostream>
#include <string>
using namespace std;

int main() {
    string S = "asisbsioaheriasdciobao";
    S.erase(remove(S.begin(), S.end(), 'a'), S.end());
    S.erase(remove(S.begin(), S.end(), 'o'), S.end());
    S.erase(remove(S.begin(), S.end(), 'i'), S.end());
    S.erase(remove(S.begin(), S.end(), 'u'), S.end());
    S.erase(remove(S.begin(), S.end(), 'e'), S.end());
    cout<<S;
}