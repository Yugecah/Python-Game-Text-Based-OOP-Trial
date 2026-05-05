class Player:
    def __init__(self, name, role, health):
        self.name = name
        self.role = role
        self.health = health
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.skills = []

    def attack(self):
        return 10 + self.level

    def gain_exp(self, amount):
        self.experience += amount
        if self.experience >= 50:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 20
        print(f"{self.name} leveled up to Level {self.level}!")

    def show_status(self):
        print("Name:", self.name)
        print("Class:", self.role)
        print("Level:", self.level)
        print("HP:", self.health)
        print("EXP:", self.experience)
        print("Inventory:", self.inventory)
