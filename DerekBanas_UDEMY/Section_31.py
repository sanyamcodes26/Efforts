import re


def initial():
    rand_str = "cat cats"
    regex = re.compile("[cat]+s?")
    print(rand_str)
    print(re.findall(regex, rand_str))

    rand_str = "doctor doctors doctor's"
    regex = re.compile("[doctor]+['s]*")
    print(rand_str)
    print(re.findall(regex, rand_str))

    rand_str = "<name>Life on Mars</name><name>Freaks and Geeks</name>"
    print(rand_str)
    regex = re.compile(r"<name>.*</name>")
    print(re.findall(regex, rand_str))
    regex = re.compile(r"<name>.*?</name>")
    print(re.findall(regex, rand_str))

    rand_str = "ape at the apex"
    print(rand_str)
    regex = re.compile(r"ape")
    print(re.findall(regex, rand_str))
    regex = re.compile(r"\bape\b")
    print(re.findall(regex, rand_str))
    return


def test():
    long_str = '''Just some words
    and some more\r
    and more'''
    print(re.findall(r"[\w\s]+[\r]?\n", long_str))
    print(re.findall("[\w\s]+[\r]?\n", long_str))
    return


if __name__ == "__main__":
    initial()
    # test()
