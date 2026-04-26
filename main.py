import random
from player import Player
from enemy import Enemy, Boss


def find_loot(player):

    loot_items = ["Medkit", "Ammo", "Armor", "Food"]
    loot = random.choice(loot_items)

    player.inventory.append(loot)

    print(f"\n You found loot: {loot}")

    if loot == "Medkit":
        player.health += 10
        print(" Medkit restored 10 health!")


def combat(player, enemy, is_final_boss=False):

    print(f"\n Enemy Appeared: {enemy.name}")
    print(f"Enemy HP: {enemy.health}")

    while enemy.health > 0 and player.health > 0:

        print("\nChoose action:")
        print("1 Attack")
        print("2 Run")

        action = input("Enter choice: ")

        
        if action == "1":

            player_damage = player.attack()
            enemy.health -= player_damage

            print(f"\n You dealt {player_damage} damage!")
            print(f"Enemy HP: {enemy.health}")

       
        elif action == "2":

            run_chance = random.randint(1, 100)

            if run_chance > 50:
                print("\n You escaped successfully!")
                return
            else:
                print("\n Escape failed!")

        else:
            print("\n Invalid action!")

       
        if enemy.health > 0:

            enemy_damage = enemy.attack()
            player.health -= enemy_damage

            print(f"{enemy.name} dealt {enemy_damage} damage to you.")
            print(f"Your HP: {player.health}")

        
        if player.health <= 0:
            print("\n You died in battle!")
            return

    
    if enemy.health <= 0:
        print(f"\n {enemy.name} defeated!")

        if not is_final_boss:
            find_loot(player)


def choose_character():

    username = input("Enter your username: ")

    print("\nChoose your character:")
    print("1 Joker (The Gunner)")
    print("2 Mysty (The Mapper)")
    print("3 Lloyd (The Medic)\n")

    choice = input("Enter choice: ")

    if choice == "1":
        player = Player(username, "Joker", "The Gunner", 120)

    elif choice == "2":
        player = Player(username, "Mysty", "The Mapper", 100)

    elif choice == "3":
        player = Player(username, "Lloyd", "The Medic", 140)

    else:
        print("Invalid choice. Default selected.")
        player = Player(username, "Mysty", "The Mapper", 100)

    print(f"\nWelcome {username}!")
    print(f"You are {player.name} ({player.role})")

    return player


def game_loop():

    player = choose_character()
    day = 1

    while day <= 25 and player.health > 0:

        print(f"\n===== DAY {day} =====")

        print("1 Explore")
        print("2 Rest")
        print("3 Status")

        choice = input("Choose action: ")

        if choice == "1":

            print("\n You explore the forest...")

           
            if day == 25:
                print("\n FINAL BOSS BATTLE ")
                enemy = Boss()
                combat(player, enemy, is_final_boss=True)
                break

            elif day % 5 == 0:
                print("\n BOSS BATTLE!")
                enemy = Boss()
            else:
                enemy = Enemy()

            combat(player, enemy)

            day += 1

        elif choice == "2":
            player.rest()
            day += 2

        elif choice == "3":
            player.show_status()

    
    if player.health <= 0:
        print("\n GAME OVER")

    elif day >= 25 and player.health > 0:
        print("\n YOU SURVIVED UNTIL DAY 25!")
        print(" FINAL BOSS COMPLETED!")
        print(" Rescue helicopter has arrived!")
        print(" Thank you for playing!")


print("==========================")
print("      THE LAST TOWER")
print("==========================")

game_loop()