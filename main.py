from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Create black magic
fire = Spell("Fire", 25, 100, "black")
thunder = Spell("Thunder", 25, 100, "black")
blizzard = Spell("Blizzard", 25, 100, "black")
meteor = Spell("Meteor", 40, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

# Create some items
potion = Item("potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super potion", "potion", "Heals 500 HP", 1000)
elixr = Item("Elixr", "elixr", "Fully restores HP/MP of one party member", 9999)
hielixr = Item("Mega-Elixr", "elixr", "Fully restores HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixr, "quantity": 5},
                {"item": hielixr, "quantity": 5},
                {"item": grenade, "quantity": 5},]
# Instantiate people
player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick:", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)
enemy = Person("Magus", 11500, 701, 1200, 34, [], [])

players = [player1, player2, player3]
running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacked" + bcolors.ENDC)

while running:
    print("*************")

    print("\n\n")

    print("NAME                                     HP                                        MP")

    for player in players:
        player.get_stats()
    print("\n")

    enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("Choose the input: ")
        print("You chose:", choice)
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)

            print("You attacked for:", dmg)

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_damage = spell.generate_damage()
            cost = spell.cost

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nYou cannot cast spell\n" + bcolors.ENDC)
                continue

            if spell.type == "white":
                player.heal(magic_damage)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for " + str(magic_damage) + " HP" + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_damage)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_damage) + " points of damage " + bcolors.ENDC)

            player.reduce_mp(cost)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n", "None left..." + bcolors.ENDC)
                continue

            item = player.items[item_choice]["item"]
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n", item.name, "heals for", str(item.prop), "HP" + bcolors.ENDC)

            elif item.type == "elixr":

                if item.name == "Mega-Elixr":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp

                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n", item.name, "fully restores HP/MP.", bcolors.ENDC)

            elif item.type == "attack":
                player.take_damage(item.prop)
                print(bcolors.FAIL + "\n", item.name, "deals", item.prop, "points of damage", bcolors.ENDC)

    enemy_choice = 1
    target = random.randrange(0, 2)
    enemy_dmg = enemy.generate_damage()
    players[target].take_damage(enemy_dmg)

    print("Enemy attacks for", enemy_dmg)
    print("____________________")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    # print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    # print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Enemy defeated you" + bcolors.ENDC)
        running = False
