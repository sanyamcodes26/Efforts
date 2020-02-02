// WAP to check A character is a vowel or consonant
# include <stdio.h>
# include <conio.h>
int is_vowel(char value){
    if(value == 'a' || value == 'e' || value == 'i' || value == 'o' || value == 'u' || value == 'A' || value == 'E' || value == 'I' || value == 'O' || value == 'U')
        return 1;
    else
        return 0;
}
int main(){
    char value;
    scanf("%c", &value);
    if(is_vowel(value) == 1)
        printf(">> True");
    else
        printf(">> False");
    return 0;
}