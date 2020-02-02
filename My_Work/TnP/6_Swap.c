// WAP to Swap two numbers without third variable
# include <stdio.h>
# include <conio.h>
int do_swap(int *value_1, int *value_2){
    *value_1 = *value_1 ^ *value_2;
    *value_2 = *value_1 ^ *value_2;
    *value_1 = *value_1 ^ *value_2;
    return 1;
}

int main(){
    int value_1, value_2;
    scanf("%d%d", &value_1, &value_2);
    printf("[%d]-[%d]", value_1, value_2);
    if(do_swap(&value_1, &value_2) == 1)
        printf("\n[%d]-[%d]", value_1, value_2);
    else
        printf(">> Try again");
    return 0;
}