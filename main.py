import random
import time
import sys

from player import Player
from enemy import Enemy, Boss
from item import Item


# ================= TYPE TEXT =================
def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ================= STORY =================
def show_story_intro():
    print("\n===== STORY =====\n")

    type_text("The story begins... you are on a boat sailing in the middle of the sea...")
    time.sleep(0.8)

    type_text("A violent storm suddenly appears...")
    time.sleep(0.8)

    type_text("CRASH!")
    time.sleep(0.8)

    type_text("Your boat sinks near a frozen island...")
    time.sleep(0.8)

    type_text("You wake up alone on a mysterious island...")
    time.sleep(0.8)

    type_text("A tall tower stands in the distance...")
    time.sleep(0.8)

    type_text("It is said to be the only safe place...")
    time.sleep(0.8)

    type_text("SURVIVE UNTIL RESCUE ARRIVES!")
    time.sleep(1)

    print("\n=================\n")


# ================= INSTRUCTIONS =================
def show_instructions():
    print("\n===== INSTRUCTIONS =====")
    print("Survive 25 days")
    print("Explore to fight enemies and collect loot")
    print("Rest to recover health (skips days)")
    print("Boss appears every 5 days")
    print("========================\n")


# ================= INVENTORY VIEW =================
def show_inventory(player):
    print("\n===== INVENTORY =====")

    if len(player.inventory.items) == 0:
        print("Inventory is empty.")
    else:
        for i, item in enumerate(player.inventory.items, 1):
            print(f"{i}. {item.name} ({item.item_type}) +{item.value}")

    print("=====================\n")


# ================= LOOT SYSTEM =================
def find_loot(player):
    loot_list = [
        Item("Medkit", "heal", 15),
        Item("Food", "heal", 10)
    ]

    loot = random.choice(loot_list)
    print(f"You found {loot.name}!")
    player.inventory.add_item(loot)


# ================= COMBAT =================
def combat(player, enemy):

    print(f"\n⚠ Enemy Appeared: {enemy.name}")

    while enemy.health > 0 and player.health > 0:

        print("\n1 Attack")
        print("2 Run")
        print("3 Use Item")

        choice = input("Choose: ")

        if choice == "1":
            dmg = player.attack()
            enemy.health -= dmg
            print(f"You dealt {dmg} damage!")

            if enemy.health <= 0:
                print(f"{enemy.name} defeated!")
                find_loot(player)
                break

            enemy_dmg = enemy.attack()
            player.health -= enemy_dmg
            print(f"{enemy.name} dealt {enemy_dmg} damage!")

        elif choice == "2":
            print("You escaped!")
            break

        elif choice == "3":
            name = input("Enter item name: ")
            player.inventory.use_item(name, player)

        else:
            print("Invalid!")


# ================= CHARACTER SELECT =================
def choose_character():

    username = input("Enter username: ")

    print("\n1 Joker (Gunner)")
    print("2 Mysty (Mapper)")
    print("3 Lloyd (Medic)")

    choice = input("Choice: ")

    if choice == "1":
        return Player(username, "Joker", "Gunner", 120)
    elif choice == "2":
        return Player(username, "Mysty", "Mapper", 100)
    elif choice == "3":
        return Player(username, "Lloyd", "Medic", 140)
    else:
        return Player(username, "Mysty", "Mapper", 100)


# ================= GAME LOOP =================
def game_loop():

    show_story_intro()
    player = choose_character()
    day = 1

    while day <= 25 and player.health > 0:

        print(f"\n===== DAY {day} =====")

        # STORY EVENTS
        if day == 1:
            type_text("You wake up injured on the island...")
        elif day == 5:
            type_text("You hear something massive moving nearby...")
        elif day == 10:
            type_text("The forest feels unnatural...")
        elif day == 15:
            type_text("You can finally see the tower...")
        elif day == 20:
            type_text("Hope of rescue is growing...")
        elif day == 25:
            type_text("A helicopter sound echoes in the sky...")

        print("\n1 Explore")
        print("2 Rest")
        print("3 Status")
        print("4 Inventory")
        print("5 Exit")

        choice = input("Choose: ")

        if choice == "1":
            enemy = Boss() if day % 5 == 0 else Enemy()
            combat(player, enemy)
            day += 1

        elif choice == "2":
            player.rest()
            day += 2

        elif choice == "3":
            player.show_status()

        elif choice == "4":
            show_inventory(player)

        elif choice == "5":
            return player

    # ================= ENDINGS =================
    if player.health <= 0:

        print("\n===== BAD ENDING =====\n")
        type_text("Your strength fades...")
        time.sleep(0.5)
        type_text("The island consumes you...")
        time.sleep(0.5)
        type_text("You did not survive.")

    else:

        print("\n===== GOOD ENDING =====\n")
        type_text("After days of survival, you reach the tower...")
        time.sleep(0.5)
        type_text("A helicopter appears in the sky...")
        time.sleep(0.5)
        type_text("You are finally rescued.")
        time.sleep(0.5)
        type_text("YOU SURVIVED THE LAST TOWER!")

    return player


# ================= MAIN MENU =================
def main_menu():

    while True:

        print("\n=== THE LAST TOWER ===")
        print("1 Start Game")
        print("2 Instructions")
        print("3 Exit")

        choice = input("Choose: ")

        if choice == "1":
            game_loop()

        elif choice == "2":
            show_instructions()

        elif choice == "3":
            break


main_menu()
