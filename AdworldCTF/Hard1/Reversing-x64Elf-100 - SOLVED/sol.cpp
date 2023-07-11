#include <bits/stdc++.h>
using namespace std;

__int64 sub_4006FD() {
    int a1;
    int i;
    __int64 v3[3]; // Changed to size 3 to match the number of strings

    v3[0] = (__int64)"Dufhbmf";
    v3[1] = (__int64)"pG`imos";
    v3[2] = (__int64)"ewUglpt";

    for (i = 0; i <= 11; ++i)
         cout <<  char(*(char*)(v3[i % 3] + 2 * (i / 3)) - 1);

}

int main() {
    char s[100];
    sub_4006FD();

    return 0;
}
