import random

# 3 enemy characters

enemy1 = {                                                  
    'name': 'Gozer the Gozerian',                       
    'level': 1,                                            
    'health': 100,
    'max_health': 150,                                          
    'equipment': {"The Ring of Gozer the Lord of the Sebouillia"},     
    'attacks': (  # TUPLE 
        ('Telepathic Push', (10, 20)),
        ('Electrokinesis Lightning', (30, 40)),
        ('Dark Magic', (40, 55))
    ),  
    'coins': {   # DICT{}
        'copper': random.randint(0, 100),                   
        'silver': random.randint(0, 100), 
        'gold': random.randint(1, 2), 
    },
    'phrases': {
        'on_attack': [' Are you a god?', "The choice is made! The Traveller has come!", 'Choose! Choose the form of the Destructor!'],     # LIST[] of Strings
        'on_defend': ['Sub-creatures!', 'Then... DIE!', 'The Choice is made!']   # LIST[] of Strings
    }
}

enemy2 = {                                                  
    'name': 'Vigo the Carpathian',                              
    'level': 1,                                             
    'health': 100,
    'max_health': 150,                                          
    'equipment': {"Vigo's Sorcerer Armor"},  # SET{}
    'attacks': (  # TUPLE 
        ('Demonic Spell', (10, 20)),
        ('Ghostly Attack', (30, 40)),
        ('Dark Magic', (40, 55))
    ),            
    'coins': { # DICT{}
        'copper': random.randint(0, 100),                   
        'silver': random.randint(0, 100), 
        'gold': random.randint(1, 2), 
    },
    'phrases': {
        'on_attack': ['[In deep, throaty voice while holding Oscar]  Now we become one.', 'Find me a child that I might live again!',
         'I, Vigo, the Scourge of Carpathia, the Sorrow of Moldavia, command you!'],  # LIST[]
        'on_defend': ["Death is but a doorway, time is but a window, I'll be back.", 
        'On a mountain of skulls, in the castle of pain, I sat on a throne of blood! What was will be! What is will be no more! Now is the season of evil!?',
         'Nooooooooo!']  # LIST[]
    }
}

enemy3 = {                                                  
    'name': 'Stay Puft Marshmallow Man',                     
    'level': 1,                                             
    'health': 100,
    'max_health': 150,                                         
    'equipment': {'Enchanted Sailors Scarf'},  # SET{} 
    'attacks': ( # TUPLE
        ('Electric Zap', (10, 20)),
        ('Electric Shock', (30, 40)),
        ('Lightning Storm', (40, 55))
    ),
    'coins': {  # DICT{}
        'copper': random.randint(0, 100),                   
        'silver': random.randint(0, 100), 
        'gold': random.randint(2, 4), 
    },
    'phrases': {
        'on_attack': ['You hear the sounds of cars being smashed under his feet as he steps closer',
         'The building shakes as he climbs!', 'Evil Growl!'],     # LIST[] of Strings
        'on_defend': ['Gggggrrrrr!', 'Sounds of shrreking in background!', 'Rrrrawwwr!']   # LIST[] of Strings
    }
}