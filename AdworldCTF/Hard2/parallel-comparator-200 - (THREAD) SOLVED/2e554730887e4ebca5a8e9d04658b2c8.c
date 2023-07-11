#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

void * checking(void *arg) {
    char *result = malloc(sizeof(char));
    char *argument = (char *)arg;
    *result = (argument[0]+argument[1]) ^ argument[2];
    return result;
}

int check(char *user_string){
    int x;
    int i;
    char taoChuoi[20 + 1];
    taoChuoi[20] = '\0';

    while ((x = rand()) >= 64);
    
    int first_letter;
    first_letter = (x % 26) + 97;

    pthread_t thread[20];
    char differences[20] = {0, 9, -9, -1, 13, -13, -4, -11, -9, -1, -7, 6, -13, 13, 3, 9, -13, -11, 6, -7};
    char *arguments[20];
    for (i = 0; i < 20; i++) {
        arguments[i] = (char *)malloc(3*sizeof(char));
        arguments[i][0] = first_letter;
        arguments[i][1] = differences[i];
        arguments[i][2] = user_string[i];

        pthread_create((pthread_t*)(thread+i), NULL, checking, arguments[i]);
    }

    void *result;
    int just_a_string[20] = {115, 116, 114, 97, 110, 103, 101, 95, 115, 116, 114, 105, 110, 103, 95, 105, 116, 95, 105, 115};
    for (i = 0; i < 20; i++) {
        pthread_join(*(thread+i), &result);
        taoChuoi[i] = *(char *)result + just_a_string[i];
        free(result);
        free(arguments[i]);
    }

    int is_ok = 1;
    for (i = 0; i < 20; i++) {
        if (taoChuoi[i] != just_a_string[i])
            return 0;
    }
    return 1;
}

int main(){
    char *user_string = (char *)calloc(20+1, sizeof(char));
    fgets(user_string, 20+1, stdin);
    int is_ok = check(user_string);
    if (is_ok)
        printf("You win!\n");
    else
        printf("Wrong!\n");
    return 0;
}
