// WAP to find out LCM of two numbers
# include <stdio.h>
# include <conio.h>

int min_val(int num_1, int num_2){
    if(num_1 < num_2)
        return num_1;
    else
        return num_2;    
}

int find_lcm(int value_1, int value_2){
    int i;
    for(i=min_val(value_1, value_2); i>=1 ; i--){
        if(value_1 % i == 0 && value_2 % i == 0)
            return i;
    }
    return i;
}

int main(){
    int value_1, value_2;
    scanf("%d%d", &value_1, &value_2);
    printf(">> %d", find_lcm(value_1, value_2));
    return 0;
}