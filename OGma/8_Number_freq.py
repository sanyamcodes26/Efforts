import random


def get_freq(lista):
    data = set(lista)
    data = list(data)
    freq = []
    data.sort()
    print("Source :\t", lista)
    print("Elements :\t", data)
    for i in data:
        count = 0
        for j in lista:
            if i == j:
                count += 1
        freq.append(count)
    return freq


if __name__ == "__main__":
    data = []
    for i in range(20):
        data.append(random.randrange(1, 10))
    print("Frequency :\t", get_freq(data))
