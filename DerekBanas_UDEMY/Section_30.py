import re


def initial():
    rand_str = "F.B.I. I.R.S. CIA"
    print(re.findall(".\..\..", rand_str))

    rand_str = '''This ia
    a long
    string
    going for
    many
    lines'''
    regex = re.compile("\n")
    print(rand_str)
    rand_str = regex.sub(" ", rand_str)
    print(rand_str)

    rand_str = "12345 670 1122"
    print(rand_str)
    print(re.findall("\d", rand_str))
    print(re.search("\d{5}", rand_str))
    print(re.findall("\d{5,7}", rand_str))

    rand_str = "412-555-4141"
    print(rand_str)
    print((re.search("\w{3}-\w{3}-\w{4}", rand_str)))
    rand_str = "412-555-414"
    print(rand_str)
    print((re.search("\w{3}-\w{3}-\w{4}", rand_str)))

    rand_str = "P Mara"
    print(rand_str)
    print(re.search("\w{2,20}\s\w{2,20}", rand_str))
    rand_str = "Pod Mara"
    print(rand_str)
    print(re.search("\w{2,20}\s\w{2,20}", rand_str))

    print(re.findall("a+", "a as ape pod mara"))
    return


def test():
    email = "db@aol.com m@.com @apple.com bd@.com"
    print(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email))
    return


if __name__ == "__main__":
    # initial()
    test()
