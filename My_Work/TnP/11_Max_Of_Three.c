// WAP to find out  Greatest of three numbers
# include <stdio.h>
# include <conio.h>

int max_val(int num_1, int num_2, int num_3){
    if(num_1 > num_2 && num_1 > num_3)
        return num_1;
    else if(num_2 > num_1 && num_2 > num_3)
        return num_2;
    else
        return num_3;
}

int main(){
    int value_1, value_2, value_3;
    scanf("%d%d%d", &value_1, &value_2, &value_3);
    printf(">> %d", max_val(value_1, value_2, value_3));
    return 0;
}