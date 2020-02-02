// WAP to find out Sum of N natural numbers
# include <stdio.h>
# include <conio.h>

int sum_of_range_natural(int num_1){
    int sum = 0, i=0;
    for(i=1; i<=num_1; i++)
        sum += i;
    return sum;
}

int main(){
    int value_1;
    scanf("%d", &value_1);
    printf(">> %d", sum_of_range_natural(value_1));
    return 0;
}