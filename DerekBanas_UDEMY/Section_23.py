def initial():
    try:
        a_list = list(range(10))
        print(a_list[12])
    except IndexError:
        print(">> Index Out Of Bounds")
    except:
        print(">> Unknown Error")

    try:
        dog_name = input("Dog name : ")
        if any(char.isdigit() for char in dog_name):
            raise Dog_Name_Error
    except Dog_Name_Error:
        print(">> Digits found..")

    num1, num2 = input("Enter two values to divide : ").split()
    try:
        quotient = int(num1) / int(num2)
        print("{} / {} = {}".format(num1, num2, quotient))
    except ZeroDivisionError:
        print(">> Can't Divide By Zero")
    else:
        print("You did't raise any exception")
    finally:
        print(">> Finally Clause")
    return


class Dog_Name_Error(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def test():
    try:
        my_file = open("my_file.txt", mode="r", encoding="utf-8")
    except FileNotFoundError as ex:
        print(">> Not Found")
        print(">>", ex.args)
    else:
        print("File :", my_file.read())
        my_file.close()
    finally:
        print(">> Done")


if __name__ == "__main__":
    # initial()
    test()
