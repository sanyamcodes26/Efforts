import random


def initial():
    rand_list = ["string", 1.434, 76, False]
    print(rand_list)
    one_to_ten = list(range(11))
    print(one_to_ten)
    rand_list = rand_list + one_to_ten
    print(rand_list)
    print(rand_list[0])
    print(len(rand_list))
    print(rand_list[:3])
    print(False in rand_list)
    print(rand_list.index(76))
    print(rand_list.count(76))


def test():
    lista = []
    for i in range(5):
        lista.append(random.randrange(1, 9))
    print(lista)


def Bubble_Sort():
    lista = []
    for i in range(10):
        lista.append(random.randrange(1, 100))
    print(lista)
    i = len(lista) - 1
    while i > 1:
        j = 0
        while j < i:
            print("{} > {} ?".format(lista[j], lista[j+1]), end=" ")
            if lista[j] > lista[j+1]:
                print("Switch")
                lista[j] = lista[j] ^ lista[j+1]
                lista[j+1] = lista[j] ^ lista[j + 1]
                lista[j] = lista[j] ^ lista[j + 1]
            else:
                print("No Switch")
            j += 1
            print(lista)
        i -= 1


if __name__ == "__main__":
    initial()
    # test()
    # Bubble_Sort()
