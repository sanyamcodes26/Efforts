// WAP to identify A number is positive or negative
// WAP to check A character is an alphabet or not
# include <stdio.h>
# include <conio.h>
int is_positive(int value){
    if(value >= 0)
        return 1;
    else
        return 0;    
}

int main(){
    int value;
    scanf("%d", &value);
    if(is_positive(value) == 1)
        printf(">> True");
    else
        printf(">> False");
    return 0;
}