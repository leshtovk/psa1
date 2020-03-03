#include <iostream>
#include <vector>
#include <string> 

using namespace std; 

int main(){

    vector<string> msg {"Hello", "World!"};

    for (const string& word : msg)
    {
        cout << word << " "; 
    }

    // build with ctrl + shift + b
    // run in terminal with .\helloworld

    cout << endl; 
}