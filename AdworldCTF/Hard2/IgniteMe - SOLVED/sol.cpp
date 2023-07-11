#include <bits/stdc++.h>
using namespace std;

int main(){
    unsigned char ida_chars[] ={
    13,  19,  23,  17,   2,   1,  32,  29,  12,   2, 
    25,  47,  23,  43,  36,  31,  30,  22,   9,  15, 
    21,  39,  19,  38,  10,  47,  30,  26,  45,  12, 
    34,   4
    };
    char flag[5];
    flag[0] = 'E';
    flag[1] = 'I';
    flag[2] = 'S';
    flag[3] = '{';
    flag[4] = '}';
    int v2 = 0;
    char fl[100] = "";
    char c[] = "GONDPHyGjPEKruv{{pj]X@rF";
    for(int i = 0; i < 24; i++){
        fl[i] = c[i] ^ ida_chars[i];
        fl[i] = (fl[i] - 72) ^ 0x55;
    }
    cout << fl << endl;
    for(int i = 0; i < 24; i++){
        if (fl[i] >= 'A' && fl[i] <= 'Z' )
            fl[i] += 32;
        else if (fl[i] <= 'a' && fl[i] >= 'z')
            fl[i] -= 32;
    }
    cout << flag[0] << flag[1] << flag[2] << flag[3] <<  fl << flag[4];
    return 0;
}