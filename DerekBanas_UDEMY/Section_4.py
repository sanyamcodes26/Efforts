import math


def test():
    miles = float(input("Miles : "))
    print("{} miles = {} kms".format(miles, miles*1.60934))


def math_funcs():
    print(math.ceil(4.85))
    print(math.floor(4.85))
    print(math.fabs(-4.85))
    print(math.factorial(5))
    print(math.fmod(14, 5))
    print(math.trunc(4.85))
    print(math.pow(2, 5))
    print(math.sqrt(199))
    print(math.pi)
    print(math.e)
    print(math.log(10000, math.e))
    print(math.log10(10000))
    print(math.sin(math.radians(90)))
    return


def initial():
    name = input("What is your name ? ")
    print("Hello!", name)
    num_1, num_2 = input("Enter 2 numbers :").split()
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 + num_2)
    print(num_1 - num_2)
    print(num_1 * num_2)
    print(num_1 / num_2)
    print(num_1 % num_2)
    print("{}".format(num_1 ** num_2))
    print("{}".format(num_1 // num_2))
    return


if __name__ == "__main__":
    initial()
    # test()
    # math_funcs()
