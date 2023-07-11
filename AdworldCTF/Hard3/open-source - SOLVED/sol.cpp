#include <bits/stdc++.h>

using namespace std;

int main(){
    int first = 0xcafe;
    int second = 25;
    char s[] = "h4cky0u";
    unsigned int hash = first * 31337 + (second % 17) * 11 + strlen(s) - 1615810207;
    printf("Get your key: ");
    printf("%x\n", hash);
    return 0;
}