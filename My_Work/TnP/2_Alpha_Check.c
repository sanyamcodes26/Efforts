// WAP to check A character is an alphabet or not
# include <stdio.h>
# include <conio.h>
int is_alpha(char value){
    if((value >= 'a' && value <= 'z') || (value >= 'A' && value <= 'Z'))
        return 1;
    else
        return 0;    
}

int main(){
    char value;
    scanf("%c", &value);
    if(is_alpha(value) == 1)
        printf(">> True");
    else
        printf(">> False");
    return 0;
}