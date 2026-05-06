import random
from Inventory import Inventory

class Player:

    def __init__(self, username, name, role, health):
        self.username = username
        self.name = name
        self.role = role
        self.health = health
        self.inventory = Inventory()

    def attack(self):
        return random.randint(10, 20)

    def rest(self):
        heal = random.randint(10, 20)
        self.health += heal
        print(f"\n{self.username} rested and recovered {heal} health.")

    def show_status(self):
        print("\n----- PLAYER STATUS -----")
        print("Username:", self.username)
        print("Character:", self.name)
        print("Role:", self.role)
        print("Health:", self.health)
        self.inventory.show_inventory()
        print("-------------------------")
