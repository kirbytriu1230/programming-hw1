#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int a, b, c, largest, smallest;
    printf("Enter three integers: ");
    if (scanf("%d %d %d", &a, &b, &c) != 3) {
        printf("Invalid input.\n");
        return 1;
    }
    largest = a;
    smallest = a;
    if (b > largest) largest = b;
    if (c > largest) largest = c;
    if (b < smallest) smallest = b;
    if (c < smallest) smallest = c;
    printf("Largest: %d\nSmallest: %d\n", largest, smallest);
    return 0;
}
