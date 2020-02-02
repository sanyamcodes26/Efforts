// WAP to find out Ascii values of a character
# include <stdio.h>
# include <conio.h>
int to_ascii(char value){
    return (int)value;
}

int main(){
    char value;
    scanf("%c", &value);
    printf(">> %d",to_ascii(value));
    return 0;
}