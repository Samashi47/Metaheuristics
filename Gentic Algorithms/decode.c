#include <stdio.h>
#include <math.h>
int main(){
    int n, dec = 0, i = 0, rem;
    float a,b,val;
    printf("Enter a binary number: ");
    scanf("%d", &n);
    printf("Enter a:");
    scanf("%f", &a);
    printf("Enter b:");
    scanf("%f", &b);
    while(n != 0){
        rem = n % 10;
        n /= 10;
        dec += rem * (1 << i);
        i++;
    }
    val = a + ((b-a)/((pow(2,i)-1)*dec));
    printf("Decimal equivalent: %d\n", dec);
    printf("Value: %f\n", val);
    return 0;
}
