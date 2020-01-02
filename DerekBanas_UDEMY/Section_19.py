import random
import math

class Warrior:
    def __init__(self, name="Default", health=0, attack_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attack_max = attack_max
        self.block_max = block_max

    def attack(self):
        return math.ceil(self.attack_max * (random.random() + 0.5))

    def block(self):
        return math.ceil(self.block_max * (random.random() + 0.5))

class Battle:
    def start_fight(self, warrior1, warrior2):
        while True:
            if self.get_attack_result(warrior1, warrior2) == "KO":
                break
            if self.get_attack_result(warrior2, warrior1) == "KO":
                break

    def get_attack_result(self, w1, w2):
        damage = w1.attack() - w2.block()
        if damage >= 0:
            w2.health = math.ceil(w2.health - damage)
            print("{} --> {} : damage : {} : Health : {}".format(w1.name, w2.name, damage, w2.health))
            if w2.health <= 0:
                print("{} died".format(w2.name))
                return "KO"
            else:
                return "GG"
        else:
            return "GG"


if __name__ == "__main__":
    thor = Warrior("Thor", 100, 10, 5)
    loki = Warrior("Loki", 100, 10, 5)
    battle = Battle()
    battle.start_fight(thor, loki)
