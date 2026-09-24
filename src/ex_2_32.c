#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    double weight, height, bmi;
    printf("Enter weight in kilograms: ");
    if (scanf("%lf", &weight) != 1 || weight <= 0) {
        printf("Weight must be positive.\n");
        return 1;
    }
    printf("Enter height in meters: ");
    if (scanf("%lf", &height) != 1 || height <= 0) {
        printf("Height must be positive.\n");
        return 1;
    }
    bmi = weight / (height * height);
    printf("BMI: %.2f\n", bmi);
    printf("BMI VALUES\n");
    printf("Underweight: less than 18.5\n");
    printf("Normal:      between 18.5 and 24.9\n");
    printf("Overweight:  between 25 and 29.9\n");
    printf("Obese:       30 or greater\n");
    return 0;
}
