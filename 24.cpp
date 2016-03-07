#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    string s = "0123456789";
    sort(s.begin(), s.end());
    long counter = 2; //initial value of s itself is the first permutation.
    while(next_permutation(s.begin(), s.end()) && (counter != 1000000)){
        cout << counter++ << "\t" << s << "\n";
    }
    cout << counter << "\t" << s <<" \n";
    return 0;
}
