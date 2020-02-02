// WAP to find out Area of a circle(radius value user given)
# include <stdio.h>
# include <conio.h>
# define PI 3.14285

int find_area_circle(float value){
    return (PI * value * value);
}

int main(){
    float value;
    scanf("%f", &value);
    printf(">> %f", find_area_circle(value));
    return 0;
}