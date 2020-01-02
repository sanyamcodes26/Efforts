import section_22_Sum as s

class Sum:
    @staticmethod
    def get_sum(*args):
        sum_1 = 0
        for i in args:
            sum_1 += i
        return sum_1


class Dog:
    num_of_dogs = 0

    def __init__(self, name="Default"):
        self.name = name
        Dog.num_of_dogs += 1

    def __str__(self):
        return "Name : {}, Total : {}".format(self.name, Dog.num_of_dogs)


if __name__ == "__main__":
    print(Sum.get_sum(1, 2, 4, 8, 7, 5))
    spocka = Dog("A")
    print(spocka)
    spockb = Dog("B")
    print(spockb)
    spockc = Dog("C")
    print(spockc)
    print(s.get_sum(1, 2, 4, 8, 7, 5))