#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

char* finalstage(char* w) {
    int h = 0;
    char* flag = (char*)malloc(1);
    flag[0] = '\0';

    for (int i = strlen(w) - 1; i >= 0; i--) {
        flag = (char*)realloc(flag, strlen(flag) + 2);

        if (i > 0) {
            flag[strlen(flag)] = w[i];
            flag[strlen(flag) + 1] = w[i - 1];
            i--;
        } else {
            flag[strlen(flag)] = w[i];
            flag[strlen(flag) + 1] = '\0';
        }
    }

    printf("Final Stage complete\n");
    return flag;
}

char* stage2(char* b) {
    char* t = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++.++++++.-----------.++++++." + (7 * 9);
    t = strtok(t, "-");
    strcat(t, "\0");

    printf("t = %s\n", t);

    for (int q = 0; q < strlen(b); q++) {
        int rand_num = rand() % 6;
        b[q] = b[q] - rand_num;
    }

    printf("Stage 2 complete\n");
    char* flag = finalstage(t);
    return flag;
}

char* stage1(char* a) {
    for (int o = 0; o < strlen(a); o++) {
        a[o] = a[o] ^ o;
    }

    char b[26];
    strcpy(b, "abcdefghijklmnopqrstuvwxyz");

    char* z = (char*)malloc(strlen(a) + 1);
    strcpy(z, a);

    for (int y = 0; y < strlen(z); y++) {
        b[y % 26] = (z[y] ^ a[y]) + 26;
    }

    printf("Stage 1 complete\n");
    char* flag = stage2(z);
    return flag;
}

int main() {
    srand(10);
    FILE* file = fopen("output.txt", "r");
    char flag[256];
    fgets(flag, sizeof(flag), file);
    fclose(file);

    printf("Length of flag: %zu\n", strlen(flag));

    char input[256];
    printf("Enter Flag: ");
    fgets(input, sizeof(input), stdin);
    input[strlen(input) - 1] = '\0';

    char* result = entry(input);

    if (strcmp(result, flag) == 0) {
        printf("Win\n");
    } else {
        printf("NOOOOOOOOOOOOOOO\n");
    }

    return 0;
}

