import re


def initial():
    rand_str = "Match everything upto @"
    print(rand_str)
    regex = re.compile(r"^.*[^@]")
    print(re.findall(regex, rand_str))

    rand_str = "@ Match everything upto"
    print(rand_str)
    regex = re.compile(r"[^@\s].*$")
    print(re.findall(regex, rand_str))

    rand_str = '''Ape is big
    Turtle is slow
    Cheetah is fast'''
    print(rand_str)
    regex = re.compile(r"(?m)^.*?\s")
    print(re.findall(regex, rand_str))

    rand_str = "My number is 412-555-1212"
    print(rand_str)
    regex = re.compile(r"412-(.*)")
    print(re.findall(regex, rand_str))

    rand_str = "My number is 412-555-1212"
    print(rand_str)
    regex = re.compile(r"412-(.*)-(.*)")
    print(re.findall(regex, rand_str))
    return


def test():
    rand_str = "412-555-1212 412-555-1245 412-555-1314"
    print(rand_str)
    regex = re.compile(r"412-(.{8})")
    print(re.findall(regex, rand_str))
    return


if __name__ == "__main__":
    initial()
    #test()
