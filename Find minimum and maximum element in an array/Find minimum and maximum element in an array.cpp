#include <iostream>

using namespace std;

int main (){
     int a[]={1,2,3,4,5,6};
     int n = 6;
     sort(a,a+n);
     pair<long long, long long>p;
     p.first=a[0];
     p.second = a[n-1];
     return p;
}