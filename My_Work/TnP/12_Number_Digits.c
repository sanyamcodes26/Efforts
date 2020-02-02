// WAP to find out Number of digits in an integer
# include <stdio.h>
# include <conio.h>

int no_of_digits(int num_1){
    int digits = 0;
    while(num_1 > 0){
        digits += 1;
        num_1 /= 10;
    }
    return digits;
}

int main(){
    int value_1;
    scanf("%d", &value_1);
    printf(">> %d", no_of_digits(value_1));
    return 0;
}