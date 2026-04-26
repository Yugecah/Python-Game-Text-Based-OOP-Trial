import random

class Enemy:

    def __init__(self):

        enemy_types = [
            ("Forest Mutant", 40, 10),
            ("Wild Beast", 35, 8),
            ("Dark Hunter", 45, 12)
        ]

        enemy = random.choice(enemy_types)

        self.name = enemy[0]
        self.health = enemy[1]
        self.damage = enemy[2]

    def attack(self):
        return random.randint(5, self.damage)


class Boss:

    def __init__(self):

        boss_types = [
            ("Forest Titan", 80, 15),
            ("Mutant King", 90, 18),
            ("Dark Guardian", 100, 20)
        ]

        boss = random.choice(boss_types)

        self.name = boss[0]
        self.health = boss[1]
        self.damage = boss[2]

    def attack(self):
        return random.randint(10, self.damage)