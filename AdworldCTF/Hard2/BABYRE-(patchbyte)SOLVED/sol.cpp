#include <bits/stdc++.h>
using namespace std;

int main(){
    char v2[100];
    v2[0] = 'f';
    v2[1] = 'm';
    v2[2] = 'c';
    v2[3] = 'd';
    v2[4] = 127;
    char v3[10] = "k7d;V`;np";
    int i;
    for (i = 0; i < strlen(v2); ++i )
        v2[i] ^= i;
    
    for(int j = 0; j < strlen(v3); i++, j++)
        v3[j] ^= i;

    cout << v2 << v3;
    
    return 0;
}