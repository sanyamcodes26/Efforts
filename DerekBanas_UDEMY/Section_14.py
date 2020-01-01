import math


def initial():
    even_list = [i*2 for i in range(10)]
    print(even_list)
    lista = list(range(1, 6))
    list_of_values = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                      for m in lista]
    print(list_of_values)
    list_of_values = [[0] * 10
                      for i in range(10)]
    print(list_of_values)


def test():
    lista = [[0] * 10
             for i in range(9)]
    for i in range(9):
        for j in range(9):
            lista[i][j] = (i + 1) * (j + 1)
    for i in range(9):
        for j in range(9):
            print(lista[i][j], end=",\t")
        print()


if __name__ == "__main__":
    # initial()
    test()
