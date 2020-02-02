// WAP to find out GCD of two numbers
# include <stdio.h>
# include <conio.h>

int find_gcd(int value_1, int value_2){
    if(value_2 == 0)
        return value_1;
    else
        return find_gcd(value_2, value_1 % value_2);
}

int main(){
    int value_1, value_2;
    scanf("%d%d", &value_1, &value_2);
    printf(">> %d", find_gcd(value_1, value_2));
    return 0;
}