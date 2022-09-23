import random
import hero
import enemy

def introduction():
    print("\nWelcome to the Ghostbuster Sim where you will play as Dr. Raymond Stantz and fight some of your most fearsom villains from the past \n\n ")
   

def battle_phase(hero, enemy):
    start = True
    while start == True:
        while hero['health'] > 0 and enemy['health'] > 0: 
            enemy_intro(enemy)
            # hero attacks
            hero_attack = hero_attack_choice()
            enemy['health'] -= hero_attack[1]
            if enemy['health'] <= 0:
                print(f"\n'{hero_attack_phrase(hero)}'You deal {hero_attack[1]} damage to {enemy['name']} with {hero_attack[0]} and it dies from the damage!")
                print(f"\nYou have defeated {enemy['name']}!")
                loot_equip_and_monies(hero, enemy)
                return
            else:
                print('\n~~~Battle~~~')
                print(f"'{hero_attack_phrase(hero)}' You deal {hero_attack[1]} damage to {enemy['name']} with {hero_attack[0]}! {enemy['name']} has {enemy['health']} health remaining.")
            # enemy attacks
            if enemy['health'] > 0:
                enemy_attack = random_enemy_attack(enemy)
                hero['health'] -= enemy_attack[1]
                if hero['health'] <= 0:
                    print(f"{enemy['name']} deals {enemy_attack[1]} damage to you with {enemy_attack[0]}! '{hero_defend_phrase(hero)}' You have 0 health remaining.")
                else:
                    print(f"{enemy['name']} deals {enemy_attack[1]} damage to you with {enemy_attack[0]}! '{hero_defend_phrase(hero)}' You have {hero['health']} health remaining. ")
            if enemy['health'] > 0 and hero['health'] <= 0:
                print(f"\nYou have been defeated by {enemy['name']}. You have failed.")
                return
        return
    else:
        return

def enemy_intro(enemy):
    if enemy['health'] == enemy['max_health']:
        print(f"\nMage: \n\
 {enemy['name']} appears from thin air, they have {enemy['health']} health. Get ready!")
        print(f"You have {hero.hero['health']} health points remaining.")
    return

def hero_attack_choice():
    start = True
    while start == True:
        print(f"\nYou have the following abilities:")
        counter = 1
        for attack in hero.hero['attacks']:
            print(f"Enter {counter} to use {attack[0]} which deals {attack[1]} damage.")
            counter += 1
        hero_attack_choice = input(f"Which ability do you use: ")
        while not hero_attack_choice.isdigit() or int(hero_attack_choice) < 1 or int(hero_attack_choice) > len(hero.hero['attacks']):
            hero_attack_choice = input(f"Enter {list(range(1, len(hero.hero['attacks']) + 1))} to select an attack! Ability choice: ".replace("[", "").replace("]", ""))
        hero_attack = hero.hero['attacks'][int(hero_attack_choice) - 1][1]
        hero_attack_name = hero.hero['attacks'][int(hero_attack_choice) -1][0]
        return hero_attack_name, hero_attack

def loot_equip_and_monies(hero, enemy):
    if hero['health'] > 0 and enemy['health'] <= 0:
        hero['equipment'].update(enemy['equipment'])
        print(f"\nEquipment collected: {list_collected_equipment(enemy)}")
        hero['coins']['copper'] = hero['coins']['copper'] + enemy['coins']['copper']
        if hero['coins']['copper'] > 100:
            hero['coins']['copper'] = hero['coins']['copper'] - 100
            hero['coins']['silver'] = hero['coins']['silver'] + 1
        hero['coins']['silver'] = hero['coins']['silver'] + enemy['coins']['silver']
        if hero['coins']['silver'] > 100:
            hero['coins']['silver'] = hero['coins']['silver'] - 100
            hero['coins']['gold'] = hero['coins']['gold'] + 1
        hero['coins']['gold'] = hero['coins']['gold'] + enemy['coins']['gold']
        print(f"Coins collected from enemy: Gold: {enemy['coins']['gold']}, Silver: {enemy['coins']['silver']}, Copper: {enemy['coins']['copper']}")
        print(f"Coin pouch new totals: {hero['coins']['gold']}G {hero['coins']['silver']}S {hero['coins']['copper']}C")
        enemy['coins']['copper'] = 0
        enemy['coins']['silver'] = 0
        enemy['coins']['gold'] = 0
    else:
        hero['equipment'].clear()
        hero['coins']['copper'] = 0
        hero['coins']['silver'] = 0
        hero['coins']['gold'] = 0
        

def list_collected_equipment(enemy):
    for stuff in enemy['equipment']:
        return stuff
        
def hero_attack_phrase(hero):
    on_attack = random.choice(hero['phrases']['on_attack'])
    return on_attack

def hero_defend_phrase(hero):
    on_defend = random.choice(hero['phrases']['on_defend'])
    return on_defend

def random_enemy_attack(enemy):
    random_attack = random.choice(enemy['attacks'])
    enemy_attack_name = random_attack[0]
    enemy_attack = random.randint(random_attack[1][0], random_attack[1][1])
    return enemy_attack_name, enemy_attack

def end_game(hero):
    if hero['health'] <= 0:
        print(f"{hero['name']} has died, you failed.")
        print('\nGame Over.\n')
        return
    if hero['health'] > 0:
        print(f"Well done {hero['name']}! You have won)")
        return
    return