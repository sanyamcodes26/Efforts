// WAP to find out  Greatest of two numbers
# include <stdio.h>
# include <conio.h>

int max_val(int num_1, int num_2){
    if(num_1 < num_2)
        return num_2;
    else
        return num_1;    
}

int main(){
    int value_1, value_2;
    scanf("%d%d", &value_1, &value_2);
    printf(">> %d", max_val(value_1, value_2));
    return 0;
}