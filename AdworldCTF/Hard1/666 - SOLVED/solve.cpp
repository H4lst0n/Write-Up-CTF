#include <bits/stdc++.h>
using namespace std;


string encode(){
    char a2[100] = "izwhroz\"\"w\"v.K\".Ni";
    char flag[100];
    int key = 18;
    for (int i = 0; i < key; i += 3 ){
        flag[i] = (key ^ *(char *)(a2 + i)) - 6;
        flag[i + 1] = (*(char *)(a2 + i + 1LL)  ^ key) + 6;
        flag[i + 2] = *(char *)(a2 + i + 2LL) ^ 6 ^ key;
    }
    return flag;
}

int main(){
    cout << encode();
    return 0;
}