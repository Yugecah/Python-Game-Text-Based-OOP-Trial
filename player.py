class Player:
    def __init__(self, name, role, health):
        self.name = name
        self.role = role
        self.health = health
        self.level = 1
        self.experience = 0
        self.inventory = []

    def attack(self):
        return 10 + self.level

    def gain_exp(self, amount):
        self.experience += amount
        if self.experience >= 50:
            self.level += 1
            self.health += 20
            print(f"{self.name} leveled up!")

    def show_status(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Level:", self.level)
        print("Health:", self.health)
        print("EXP:", self.experience)
        print("Inventory:", self.inventory)
