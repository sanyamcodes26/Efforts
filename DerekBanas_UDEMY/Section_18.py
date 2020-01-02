class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        self.weight -= 1
        print("Run {} Run..Bhaw Bhaw".format(self.name))

    def eat(self):
        self.weight += 1
        print("Eat {} Eat..Bhaw Bhaw".format(self.name))

    def bark(self):
        print("Bhaw Bhaw".format(self.name))


class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print(">> Height :")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print(">> Only numbers plz")

    @property
    def width(self):
        print(">> Width :")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit:
            self.__width = value
        else:
            print(">> Only numbers plz")

    def get_area(self):
        return int(self.height) * int(self.width)


if __name__ == "__main__":
    spot = Dog("Spott", 66, 26)
    spot.eat()
    spot.bark()
    spot.run()

    square = Square()
    height, width = input(">> ").split()
    square.height = height
    square.width = width
    print("Height :", square.height)
    print("Width :", square.width)
    print("Area :", square.get_area())