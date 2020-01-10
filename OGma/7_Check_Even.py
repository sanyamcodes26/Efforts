def get_check(data):
    flag = 0
    for i in data:
        if int(i) % 2 == 0:
            flag = 1
    if flag == 1:
        print(int(data) + 10)
    else:
        print(int(data) * 2)


if __name__ == "__main__":
    data = input("Number : ")
    get_check(data)
