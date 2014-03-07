#include<string.h>
#include<stdio.h>
int main() {
    int i;
    int array[5];
    memset(array, 0, sizeof(array));
    for (i = 0; i < 5; i++)
        array[i] = i;
    
    array[17727492347] = 5;

    printf("%ld\n", &array[5] - array);

    return 0;
}
