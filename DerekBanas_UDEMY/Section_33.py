import re


def initial():
    rand_str = "1. Dog 2. Cat 3. Turtle"
    print(rand_str)
    regex = re.compile(r"\d\.\s(Dog|Cat)")
    print(re.findall(regex, rand_str))

    rand_str = "11-23-2014"
    print(rand_str)
    regex = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", rand_str)
    print(regex.group())
    print(regex.group(1))
    print(regex.group(2))
    print(regex.group(3))

    regex = re.search("\d{2}", "The weight eas 32 kgs")
    print(regex.group())
    print(regex.span())
    print(regex.start())
    print(regex.end())

    rand_str = "January 01 1998"
    print(rand_str)
    regex = r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)"
    matches = re.search(regex, rand_str)
    print(matches.group())
    print(matches.group('month'))
    print(matches.group('day'))
    print(matches.group('year'))
    return


def test_1():
    rand_str = "12345 12345-1234 1234 123456-333"
    print(rand_str)
    regex = re.compile(r"\d{5}-\d{4}|\d{5}\s")
    print(re.findall(regex, rand_str))
    return


def test_2():
    rand_str = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
    regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    matches = re.findall(regex, rand_str)
    print(rand_str)
    print(matches)
    return


def test_3():
    rand_str = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
    print(rand_str)
    regex = r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\))?(\d{3})(-| )?(\d{4}|\d{4}))"
    match = re.findall(regex, rand_str)
    print(match)
    return


if __name__ == "__main__":
    # initial()
    # test_1()
    # test_2()
    test_3()
