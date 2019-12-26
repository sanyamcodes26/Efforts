import random


def initial():
    rand_num = random.randrange(1, 51)
    i = 1
    while i != rand_num:
        i += 1
    print("Found for : ", i)
    i = 1
    while i <= 20:
        if i % 2 == 0:
            i += 1
            continue
        if i == 15:
            break
        print(i, end=" ")
        i += 1
    print()
    return


def test():
    rows = int(input("Rows : "))
    i = 1
    while i <= rows:
        j = 1
        while j <= rows - i:
            print(end=" ")
            j += 1
        j = 1
        while j <= i * 2 - 1:
            print(end="#")
            j += 1
        print()
        i += 1
    i = 1
    while i < rows:
        print(end=" ")
        i += 1
    print("#")
    return


if __name__ == "__main__":
    initial()
    # test()
