import sys


def initial():
    my_age = 41
    my_name = "Akash"
    print("Hello", my_name, my_age, "years old")
    # Single line comment
    '''Multi-line Comment
    Python
    is
    dynamically
    typed'''
    str_1 = "\"Quote\""
    print(str_1)
    print("Max int", sys.maxsize)
    print("Max float", sys.float_info.max)
    complex_number = 5 + 6j
    print("Complex", complex_number)
    print(type(int(34.544)))
    print(type(str(34.544)))
    # Character to unicode
    print(type(ord('c')))
    num_1 = "34"
    num_2 = "43"
    print(num_1, "+", num_2, "=", int(num_1) + int(num_2))
    return


if __name__ == "__main__":
    initial()
