import random


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def generator_prime(max_num):
    for num in range(2, max_num):
        if is_prime(num):
            yield num
    return


double = (x * 2
          for x in range(10))


def initial():
    print(list(map((lambda x: x * 2), range(1, 11))))
    print([2 * x
           for x in range(1, 11)])

    print(list(filter((lambda x: x % 2 != 0), range(1, 11))))
    print([x
           for x in range(1, 11)
           if x % 2 != 0])

    print([i ** 2
           for i in range(50)
           if i % 8 == 0])
    print([x * y
           for x in range(1, 3)
           for y in range(11, 16)])
    print([x
           for x in [i * 2
                     for i in range(10)]
           if x % 8 == 0])

    multi_list = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    print([col[1]
          for col in multi_list])
    print([multi_list[i][i]
           for i in range(len(multi_list))])

    prime = generator_prime(50)
    print("Prime :", next(prime))
    print("Prime :", next(prime))
    print("Prime :", next(prime))
    print("Prime :", next(prime))
    print("Prime :", next(prime))

    print("Double :", next(double))
    print("Double :", next(double))
    print("Double :", next(double))
    print("Double :", next(double))
    print("Double :", next(double))
    return


def test():
    print([x
           for x in [random.randrange(1, 1001)
                     for i in range(50)]
           if x % 9 == 0])
    return


if __name__ == "__main__":
    initial()
    # test()
