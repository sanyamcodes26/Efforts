class Math_py:
    def __init__(self, data=0):
        self.num = data

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, data=0):
        self._num = data

    def power(self):
        return self.num ** 6

    def fact(self):
        temp = self.num
        data = 1
        while temp > 0:
            data *= temp
            temp -= 1
        return data


if __name__ == "__main__":
    while True:
        try:
            data = input("Number : ")
            if data == "N":
                break
            data = int(data)
        except ValueError:
            print("Give number as input")
        else:
            m = Math_py(data)
            print("---")
            print("Power :", m.power())
            print("Factorial :", m.fact())
            print("---")
