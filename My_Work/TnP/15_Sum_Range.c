// WAP to find out Sum of numbers in a given range
# include <stdio.h>
# include <conio.h>

int sum_of_range(int num_1, int num_2){
    int sum = 0, i=0;
    for(i=num_1; i<=num_2; i++)
        sum += i;
    return sum;
}

int main(){
    int value_1, value_2;
    scanf("%d", &value_1, &value_2);
    printf(">> %d", sum_of_range(value_1, value_2));
    return 0;
}