def mult_by_2(num):
    return num * 2


def do_math(func, num):
    return func(num)


def func_mult_num(num):
    def muly_by(value):
        return num * value
    return muly_by


def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def change_list(lista, func):
    odd_list = []
    for i in lista:
        if func(i):
            odd_list.append(i)
    return odd_list


def test():
    a_list = list(range(1, 22))
    print(change_list(a_list, is_it_odd))
    return


if __name__ == "__main__":
    times_two = mult_by_2
    print(times_two(22.22))
    print(do_math(times_two, 22.22))
    print(func_mult_num(22.22))
    test()
