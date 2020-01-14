class Vehicle:
    def __init__(self):
        print("Automobile")


class Bugati(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        print("Buggati")


class Hummer(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        print("Hummer")


class Maruti(Hummer, Bugati):
    def __init__(self):
        Hummer.__init__(self)
        Bugati.__init__(self)
        print("Maruti")


car = Vehicle()
print("-" * 10)
car = Hummer()
print("-" * 10)
car = Bugati()
print("-" * 10)
car = Maruti()
print("-" * 10)
