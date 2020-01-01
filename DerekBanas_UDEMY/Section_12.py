def mul_divide(num_1, num_2):
    return (num_1 * num_2), (num_1 // num_2)


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def list_of_primes(num1, num2):
    lista = []
    for i in range(num1, num2 + 1):
        if is_prime(i):
            lista.append(i)
    return lista


def sum_all(*args):
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1


def rectangle_area():
    print("rectangle")
    return


def circle_area():
    print("circle")
    return 


def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Error")
    return


def initial():
    print(mul_divide(5, 4))
    print(list_of_primes(45, 230))
    print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(get_area("circle"))


if __name__ == "__main__":
    initial()
