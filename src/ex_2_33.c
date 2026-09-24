#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    double distance, fuel_price, efficiency, parking, tolls, cost;
    printf("Total kilometers driven per day: ");
    if (scanf("%lf", &distance) != 1 || distance < 0) return 1;
    printf("Fuel cost per liter: ");
    if (scanf("%lf", &fuel_price) != 1 || fuel_price < 0) return 1;
    printf("Average kilometers per liter: ");
    if (scanf("%lf", &efficiency) != 1 || efficiency <= 0) {
        printf("Fuel efficiency must be positive.\n");
        return 1;
    }
    printf("Parking fees per day: ");
    if (scanf("%lf", &parking) != 1 || parking < 0) return 1;
    printf("Tolls per day: ");
    if (scanf("%lf", &tolls) != 1 || tolls < 0) return 1;
    cost = distance / efficiency * fuel_price + parking + tolls;
    printf("Daily driving cost: %.2f\n", cost);
    return 0;
}
