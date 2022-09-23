import functions
import hero
import enemy

def run_game():
    functions.introduction()
    functions.battle_phase(hero.hero,enemy.enemy1)
    functions.battle_phase(hero.hero,enemy.enemy2)
    functions.battle_phase(hero.hero,enemy.enemy3)
    functions.end_game(hero.hero)
run_game()