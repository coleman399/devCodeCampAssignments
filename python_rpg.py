# You are Hercules, the greatest of the Greek Heroes! You have been tasked by King
# Eurystheus to slay the vicious Nemean Lion, defeat the impossible nine-headed
# Lernaean Hydra, and capture the guard dog of the underworld—Cerberus
import random
#values - health etc.
hercules = {
    "name": "Hercules",
    "health": 20,
    "attack power": random.randint(1, 8),
}
nemean_lion = {
    "name": "Nemean Lion",
    "health": 10,
    "attack power": random.randint(1, 5),
    "attack name": ["bite", "claw", "pounce"]
}
lernaean_hydra = {
    "name": "Lernaean Hydra",
    "health": 10,
    "attack power": random.randint(1, 5),
    "attack name": ["multi-bite","head regrowth", "scream"]
}
def random_element_from_list(list):
    list_index = random.randint(0, len(list)-1)
    return list_index
def attack_menu(enemy):
    print("***** ATTACKS *****")
    print("[1] Charge")
    print("[2] Boulder Throw")
    print("[3] Sword Swing")
    print("-------------------")
    while True:
        user_input = input()
        if user_input == "1":
            print("Hercules used Charge!")
            return attack(enemy)
        elif user_input == "2":
            print("Hercules used Boulder Throw!")
            return attack(enemy)
        elif user_input == "3":
            print("Hercules used Sword Swing!")
            return attack(enemy)
        else:
            print("Please use the [1], [2], or [3] keys to make a selection.")
def attack(enemy):
    while True:
        enemy['health'] = enemy['health'] - hercules['attack power']
        print(f"Hercules deals {hercules['attack power']} to {enemy['name']}") 
        enemy_attack_index = random_element_from_list(enemy['attack name'])
        print(f"{enemy['name']} used {enemy['attack name'][enemy_attack_index]}!")
        hercules['health'] = hercules['health'] - enemy['attack power']
        print(f"{enemy['name']} deals {enemy['attack power']} to Hercules")
        if enemy['health'] > 0 and hercules['health'] > 0:
            print(f"{enemy['name']} has {enemy['health']} health left!")
            print(f"{hercules['name']} has {hercules['health']} health left!")
            attack_menu(enemy)
        if enemy['health'] <= 0 or hercules['health'] <= 0:
            if enemy['health'] <= 0:
                return 0
            else:
                return 1
def play_game():
    print("You are Hercules, the greatest of the Greek Heroes! You have been tasked by King Eurystheus to slay the vicious Nemean Lion,\ndefeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.")
    print("First Battle! YOU vs The Nemean Lion!")
    if attack_menu(nemean_lion) == 0:
        print("You have won the battle!")
        print("Second Battle!\nYOU vs The Impossible Nine-Headed Lernaean Hydra!")
        if attack_menu(lernaean_hydra) == 0:
            print("You have won the battle!")
            print("You capture the guard dog of the underworld—Cerberus and live happily ever after.")
        else:
            print("You were defeated.")
    else:
        print("You were defeated.")

play_game()


