from classes.game import Person, bcolors
from classes.magic import Spell

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = Person(1200, 65, 45, 34, [])


running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacked" + bcolors.ENDC)

while running:
    print("*************")
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

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()

    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)
    print("____________________")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Enemy defeated you" + bcolors.ENDC)
        running = False
