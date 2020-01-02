class test:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        num = self.first + self.second
        self.first = self.second
        self.second = num
        return num


class Alphabet:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]


def initial():
    samp_string = iter("Sample")
    print("Char :", next(samp_string))
    print("Char :", next(samp_string))
    print("Char :", next(samp_string))
    print("Char :", next(samp_string))
    alpha = Alphabet()
    for letter in alpha:
        print(letter, end=" ")
    print()
    return


if __name__ == "__main__":
    # initial()
    fib = test()
    for i in range(10):
        print("FIB :", next(fib))
