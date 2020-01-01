def factorial_1(num):
    if num <= 1:
        return 1
    else:
        return num * factorial_1(num - 1)


def test_fibonacci_1(num):
    if num == 1 or num == 0:
        return num
    else:
        return test_fibonacci_1(num - 1) + test_fibonacci_1(num - 2)


def test2(num):
    i = 1
    while i <= num:
        print(test_fibonacci_1(i))
        i += 1


def initial():
    print("factorial(7) :", factorial_1(7))
    print(test_fibonacci_1(10))
    print(test2(10))
    return


if __name__ == "__main__":
    initial()
