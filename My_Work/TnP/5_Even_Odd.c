// WAP to identify A number is even or odd
# include <stdio.h>
# include <conio.h>
int is_even(int value){
    if(value % 2 == 0)
        return 1;
    else
        return 0;    
}

int main(){
    int value;
    scanf("%d", &value);
    if(is_even(value) == 1)
        printf(">> True");
    else
        printf(">> False");
    return 0;
}