#include <bits/stdc++.h>
using namespace std;

int main(){
    char ida_chars[100] ={
    158, 231,  48,  95, 167,   1, 166,  83,  89,  27, 
    10,  32, 241, 115, 209,  14, 171,   9, 132,  14, 
    141,  43};
    for(int i = 0; i < strlen(ida_chars); i++)  
        ida_chars[i] ^= 0x22;
    cout << ida_chars;
    return 0;
}