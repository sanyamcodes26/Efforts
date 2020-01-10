def is_prime(num):
    num = int(num)
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_multipliers(num):
    num = int(num)
    lista = [1]
    for i in range(2, num + 1):
        if num % i == 0:
            lista.append(i)
    return lista


if __name__ == "__main__":
    # lista = list(input("Type numbers : ").split())
    lista = [i for i in range(1, 101)]
    for i in lista:
        if is_prime(i):
            print(f"{int(i)}\t->\t{int(i) ** 2}")
        else:
            data = get_multipliers(i)
            print(f"{int(i)}\t->\t{data}")
