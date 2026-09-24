#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int first, second;
    printf("Enter two integers: ");
    if (scanf("%d %d", &first, &second) != 2) {
        printf("Invalid input.\n");
        return 1;
    }
    if (second == 0) {
        printf("The second integer must not be zero.\n");
        return 1;
    }
    /* Avoid INT_MIN % -1, which is not representable as an int division. */
    if (second == -1 || first % second == 0)
        printf("%d is a multiple of %d.\n", first, second);
    else
        printf("%d is not a multiple of %d.\n", first, second);
    return 0;
}
