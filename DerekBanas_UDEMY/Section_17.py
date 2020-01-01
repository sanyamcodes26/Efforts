import os


def initial_1():
    with open("my_file.txt", mode="w", encoding="utf-8") as fp:
        fp.write(input("Type anything : "))
    print(fp.closed)
    with open("my_file.txt", mode="r", encoding="utf-8") as fp:
        print(fp.read())
        print(fp.name)
        print(fp.mode)
    # os.rename("my_file.txt", "test.dat")
    # os.rename("test.dat", "my_file.txt")
    # os.mkdir("My_dir")
    # os.chdir("My_dir")
    print(os.getcwd())
    # os.chdir("..")
    # os.rmdir("My_dir")
    print(fp.closed)
    with open("my_file.txt", mode="r", encoding="utf-8") as fp:
        line_n = 1
        while True:
            line = fp.readline()
            if not line:
                break
            print("Line {} : {}".format(line_n, line), end="")
            line_n += 1
    return


def initial_2():
    my_tuple = tuple(range(1, 11))
    print(my_tuple)
    return


def test():
    with open("my_file.txt", mode="r", encoding="utf-8") as fp:
        line_n = 1
        while True:
            line = fp.readline()
            if not line:
                break
            print("Line :", line_n)
            word_list = line.split()
            print("Words :", len(word_list))
            char_ct = 0
            for word in word_list:
                for char in word:
                    char_ct += 1
            print("Average count :", char_ct // len(word_list))
            line_n += 1
    return


if __name__ == "__main__":
    # initial_1()
    # test()
    initial_2()
