#include <iostream>
#include <string>
using namespace std;

int main (){

    string type = "concave";
    float R = 3,12;
    if (type == "concave"){
        cout<<floor(R/2);}
    else if (type == "convex"){
        cout<<floor(-(R/2));}

}