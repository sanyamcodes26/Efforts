def pattern_1():
    l_list = (1, 1, 1, 1, 4)
    i_list = (1, 1, 1, 1, 1)
    f_list = (4, 1, 2, 1, 1)
    e_list = (4, 1, 2, 1, 4)
    choice = input(">> Choice Character : ")
    for i in l_list:
        print(choice * i)
    print()
    for i in i_list:
        print(choice * i)
    print()
    for i in f_list:
        print(choice * i)
    print()
    for i in e_list:
        print(choice * i)
    return


def pattern_2():
    choice = input(">> Choice Character : ")
    print(choice)
    for j in range(2):
        for i in range(4):
            print(choice, " " * i, choice)
        for i in range(4, -1, -1):
            print(choice, " " * i, choice)
        print(choice)

    return


if __name__ == "__main__":
    # pattern_1()
    pattern_2()
