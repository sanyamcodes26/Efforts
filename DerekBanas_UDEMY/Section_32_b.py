import re


def initial():
    rand_str = "The cat cat fell out of the window"
    print(rand_str)
    regex = re.compile(r"(\b\w+)\s+\1")
    print(re.findall(regex, rand_str))

    rand_str = "<a href = '#><b>The Link</b></a>"
    print(rand_str)
    regex = re.compile(r"<b>(.*?)</b>")
    rand_str = re.sub(regex, r"\1", rand_str)
    print(rand_str)

    rand_str = "412-555-1212"
    print(rand_str)
    regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
    rand_str = re.sub(regex, r"(\1)\2", rand_str)
    print(rand_str)

    rand_str = "One two three four"
    print(rand_str)
    regex = re.compile(r"\w+(?=\b)")
    print(re.findall(regex, rand_str))

    rand_str = "1. Bread 2. Apple 3. Dong"
    print(rand_str)
    regex = re.compile(r"(?<=\d.\s)\w+")
    print(re.findall(regex, rand_str))

    rand_str = "<h1>I am important</h1> <h1>So am I</h1>"
    print(rand_str)
    regex = re.compile(r"(?<=<h1>).+?(?=</h1>)")
    print(re.findall(regex, rand_str))

    rand_str = "8 apples $3, 1 Bread $1, 1 Cereal $4"
    print(rand_str)
    regex = re.compile(r"(?<!\$)\d+")
    print(re.findall(regex, rand_str))
    return


def test():
    rand_str = "https://www.youtube.com http://www.google.com"
    print(rand_str)
    regex = re.compile(r"(https?://([\w.]+))")
    rand_str = re.sub(regex, r"<a href = '\1'>\2</a>\n", rand_str)
    print(rand_str)
    return


if __name__ == "__main__":
    initial()
    # test()
