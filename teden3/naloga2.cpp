#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

vector<int> split(string inp_str, string delimiter) {
    vector<int> result;
    size_t pos = 0;
    while ((pos = inp_str.find(delimiter)) != string::npos) {
        result.push_back(stoi(inp_str.substr(0, pos)));
        inp_str.erase(0, pos + delimiter.length());
    }
    result.push_back(stoi(inp_str));

    return result;
}

void count_nbs(vector<int> nbd, int D){
    int counter = 0;
    for (vector<int>::iterator it1 = nbd.begin(); it1 < nbd.end(); ++it1){
        for (vector<int>::iterator it2 = it1 + 1; it2 < nbd.end(); ++it2){
            if (abs(*it1 - *it2) <= D) {
                counter = counter + 1;
            }
        }
    }
    cout << counter;
}

int main() {

    string line1, line2;
    getline (cin, line1);
    getline (cin, line2);

    vector<int> ln1 = split(line1, " ");
    vector<int> nbd = split(line2, " ");
    int D = ln1[1];
    count_nbs(nbd, D);

    return 0;
}


