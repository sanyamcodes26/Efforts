import random
from functools import reduce

sum_1 = lambda x, y: x + y
can_vote = lambda age: True if age >= 18 else False
power_list = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
double_num = lambda x: x * 2


def test():
    lista = []
    for i in range(100):
        lista.append(random.randrange(1, 1000))
    print(lista)
    print(list(filter((lambda x: x % 9 == 0), lista)))


def initial():
    print(sum_1(25, 44))
    print(can_vote(14))
    for func in power_list:
        print(func(3))
    func = random.choice(power_list)
    print(func(5))

    lista = list(range(3, 14))
    print(list(map(power_list[2], lista)))
    print(list(map(sum_1, lista, lista)))

    print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

    print(reduce((lambda x, y: x + y), lista))
    return


if __name__ == "__main__":
    initial()
    # test()
