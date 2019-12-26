def initial():
    sample_str = "Sample String"
    print(len(sample_str))
    print(sample_str[2])
    print(sample_str[1:])
    print(sample_str[:7])
    print(sample_str[1:8])
    print(sample_str[0:-1:2])
    # reverse of a string
    print(sample_str[::-1])
    print("A = ", ord("A"))
    print("65 = ", chr("A"))
    return


def test_1():
    inp_str = (input("Type (no space) : ")).upper()
    encrypt = ""
    for i in inp_str:
        encrypt += str(ord(i))
    print(encrypt)
    out_str = ""
    for i in range(0, len(encrypt)-1, 2):
        out_str += chr(int(encrypt[i]+encrypt[i+1]))
    print(out_str)
    return


def test_2():
    inp_str = (input("Type (no space): "))
    encrypt = ""
    for i in inp_str:
        encrypt += str(ord(i) - 23)
    print(encrypt)
    out_str = ""
    for i in range(0, len(encrypt) - 1, 2):
        out_str += chr(int(encrypt[i] + encrypt[i + 1]) + 23)
    print(out_str)
    return


if __name__ == "__main__":
    # initial()
    # test_1()
    test_2()

