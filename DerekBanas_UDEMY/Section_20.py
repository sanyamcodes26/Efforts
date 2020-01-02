class Animal:
    def __init__(self, birth_type="Unknown", appearence="Unknown", blodded="Unknown"):
        self.__birth_type = birth_type
        self.__appearence = appearence
        self.__blooded = blodded

    @property
    def birth_type(self):
        return self.__birth_type

    @birth_type.setter
    def birth_type(self, value):
        self.__birth_type = value

    @property
    def appearence(self):
        return self.__appearence

    @birth_type.setter
    def appearence(self, value):
        self.__appearence = value

    @property
    def blodded(self):
        return self.__blooded

    @birth_type.setter
    def blodded(self, value):
        self.__blooded = value

    def __str__(self):
        return "Is a {} with {} blood and appearence {}".format(self.birth_type, self.blodded, self.appearence)


class Mammal(Animal):
    def __init__(self, birth_type="Born Alive", appearence="Hair/Fur", blodded="Warm", nurse_young=True):
        Animal.__init__(birth_type, appearence, blodded)
        self.__nurse_young = nurse_young

    @property
    def nurse_young(self):
        return self.__nurse_young

    @nurse_young.setter
    def nurse_young(self, value):
        self.__nurse_young = value

    def __str__(self):
        return super().__str__() + " and they {}".format(self.nurse_young)


class Reptile(Animal):
    def __init__(self, birth_type="In Egg", appearence="Dry Scales", blodded="Cold"):
        Animal.__init__("Reptile", birth_type, appearence, blodded)


if __name__ == "__main__":
    animal = Animal()
    print(animal)
    mammal = Mammal()
    print(mammal)
    reptile = Reptile()
    print(reptile)
