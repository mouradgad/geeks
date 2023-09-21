#include <iostream> 
#include <vector>
using namespace std;

int main() {
    string S; 
    cout << "Enter a string: ";
    cin >> S; 
    
    vector<string> s;

    int n = S.length();
    string p = "";
    while (n > 0) {
        for (int i = 0; i < n; i++)
            p = p + S[i];
        s.push_back(p);
        n--;
        p = "";
    }

    for (const string& str : s) {
        cout << str <<"\n";
    }

}
