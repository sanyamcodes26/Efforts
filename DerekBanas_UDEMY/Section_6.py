def initial():
    for i in range(10):
        print(i, end=" ")
    print()
    num = int(input("Number : "))
    print("Even : ", (num % 2 == 0))
    for i in range(num):
        print(i, (i % 2 == 0), end=" ")
    print()
    num_float = float(input("Number Float : "))
    print("Rounded to 2 decimal places : {:.2f}".format(num_float))
    return


def test():
    money = float(input("Investment : "))
    rate = float(input("Rate : ")) * 0.01
    for i in range(10):
        money = money + money * rate
    print("Amount : {:.2f}".format(money))
    return


if __name__ == "__main__":
    initial()
    # test()
