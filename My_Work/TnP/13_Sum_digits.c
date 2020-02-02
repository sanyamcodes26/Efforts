// WAP to find out Sum of digits of a number
# include <stdio.h>
# include <conio.h>

int sum_of_digits(int num_1){
    int sum = 0;
    while(num_1 > 0){
        sum += num_1 % 10;
        num_1 /= 10;
    }
    return sum;
}

int main(){
    int value_1;
    scanf("%d", &value_1);
    printf(">> %d", sum_of_digits(value_1));
    return 0;
}