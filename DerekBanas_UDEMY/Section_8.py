import random
from decimal import Decimal as D


def initial():
    while True:
        try:
            number = int(input("Number : "))
            break
        except ValueError:
            print("Enter a Number")
        except:
            print("Unknown error")
    return


def decimal_func():
    sum_1 = D(0)
    sum_1 += D("0.0000000011111111")
    sum_1 += D("0.1111111100000000")
    print(sum_1)
    sum_1 -= D("0.1111111111111111")
    print(sum_1)
    return


def test():
    key_num = random.randrange(1, 11)
    while True:
        while True:
            try:
                num = int(input("Between 1 and 10 : "))
                break
            except:
                print("Error")
        if num == key_num:
            print("Correct")
            break
    return


if __name__ == "__main__":
    initial()
    # test()
    # decimal_func()
