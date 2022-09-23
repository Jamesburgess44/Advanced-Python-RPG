hero = {                                                    
    'name': 'Dr. Raymond Stantz',                                             
    'level': 1,                                             
    'health': 100,                                          
    'equipment': {"Proton Pack"}, # SET{}
    'attacks': ( # TUPLE 
        ('Low Power', 25),
        ('Normal Power', 50),
        ('Maxium Power', 100)
    ),        
    'coins': {# DICT{}
        'copper': 0,                                        
        'silver': 0, 
        'gold': 0, 
    },
    'phrases': {
        'on_attack': ["This man has no dick!", 'All right! This chick is TOAST!', 'We came, we saw, we kicked its ass!'],     # LIST[] 

        'on_defend': ["I'm fuzzy on the whole good/bad thing. What do you mean, 'bad'?",
         "We've been going about this all wrong. This Mr. Stay Puft's okay! He's a sailor, he's in New York; we get this guy laid, we won't have any trouble!",
          "Ray has gone bye-bye, Egon... what've you got left?"] # LIST[] 
    }
}