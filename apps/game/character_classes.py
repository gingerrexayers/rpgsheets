class Characterclass() = {
    'name':'',
    ###description###
    'look':{
        'body':[],
        'eyes':[],
        'decoration':[],
        'clothes':[]
    },
    'alignment':{
        'type1':{
            'title':'',
            'description':''''''
        }
        'type2':{
            'title':'',
            'description':''''''
        }
    },
    'bonds':{
        'name':'',
        'type':[]
    }
    'race':{
        'type1':{
            'name':'',
            'description':''''''
        }
    },
    ###stats###
    'armor':'',
    'hitpoints':'',
    'damage':'',
    'level':'',
    'xp':'',
    'coin':'',
    'strength':{
        'value':'',
        'condition':''
    }
    'dexterity':{
        'value':'',
        'condition':''
    }
    'constitution':{
        'value':'',
        'condition':''
    }
    'intelligence':{
        'value':'',
        'condition':''
    }
    'wisdom':{
        'value':'',
        'condition':''
    }
    'charisma':{
        'value':'',
        'condition':''
    }
    ###starter moves and advanced moves###
    'moves':{
        'default':{
            'move1':{
                'name':'',
                'description':'''''',
                'action':''
            },
            'move2':{
                'name':'',
                'description':'''''',
                'action':''
            },
            
        },
        'level1':{
            'move1':{
                'name':'',
                'description':''''''
            },
            'move2':{
                'name':'',
                'description':''''''
            },
            'move3':{
                'name':'',
                'description':''''''
            },
            'move4':{
                'name':'',
                'description':''''''
            }
        },
        'level2':{
            'move1':{
                'name':'',
                'description':''''''
            },
            'move2':{
                'name':'',
                'description':''''''
            },
            'move3':{
                'name':'',
                'description':''''''
            },
            'move4':{
                'name':'',
                'description':''''''
            },
            'move5':{
                'name':'',
                'description':''''''
            },
            'move6':{
                'name':'',
                'description':''''''
            },
            'move7':{
                'name':'',
                'description':''''''
            },
            'move8':{
                'name':'',
                'description':''''''
            },
            'move9':{
                'name':'',
                'description':''''''
            },
            'move10':{
                'name':'',
                'description':''''''
            },
            'move11':{
                'name':'',
                'description':''''''
            },
            'move12':{
                'name':'',
                'description':''''''
            },
        },
        'level6':{
            'move1':{
                'name':'',
                'description':''''''
            },
            'move2':{
                'name':'',
                'description':''''''
            },
            'move3':{
                'name':'',
                'description':''''''
            },
            'move4':{
                'name':'',
                'description':''''''
            },
            'move5':{
                'name':'',
                'description':''''''
            },
            'move6':{
                'name':'',
                'description':''''''
            },
            'move7':{
                'name':'',
                'description':''''''
            },
            'move8':{
                'name':'',
                'description':''''''
            },
            'move9':{
                'name':'',
                'description':''''''
            },
            'move10':{
                'name':'',
                'description':''''''
            },
            'move11':{
                'name':'',
                'description':''''''
            },
            'move12':{
                'name':'',
                'description':''''''
            },
        }
    }
    
}

class Barbarian() = {
    'name':'barbarian',
    ###description###
    'look':{
        'body':['mighty thews','long shanks','scrawny','supple'],
        'eyes':['tormented','haunted','wild','shrouded'],
        'decoration':['tattoos','bejeweled','unmarred'],
        'clothes':["scraps","silks","scavenger's outfit","weather-inapporpriate"]
    },
    'alignment':{
        'chaotic':{
            'title':'Chaotic',
            'description':'Eschew a convention of the civlized world.'
        },
        'neutral':{
            'title':'Neutral',
            'description':'Teach someone the ways of your people'
        }
    },
    'bonds':{
        'name':'',
        'type':[" is puny and foolish, but amusing to me.", "'s ways are strange and confusing.", " is always getting into trouble.  I must protect them from themselves.", " shares my hunger for glory; the earth will tremble at our passing!"]
    }
    'race':{
        'outsider':{
            'name':'Outsider',
            'description':"You may be elf, dwarf, halfing, or human, but you and your people are not from around here.  At the beginning of each session, the GM will as you something about your homeland, why you left, or what you left behind.  if you answer them, mark XP"
        }
    },
    ###stats###
    'armor':'',
    'hitpoints':'',
    'damage':'',
    'level':'',
    'xp':'',
    'coin':'',
    'strength':{
        'value':'',
        'condition':''
    }
    'dexterity':{
        'value':'',
        'condition':''
    }
    'constitution':{
        'value':'',
        'condition':''
    }
    'intelligence':{
        'value':'',
        'condition':''
    }
    'wisdom':{
        'value':'',
        'condition':''
    }
    'charisma':{
        'value':'',
        'condition':''
    }
    ###starter moves and advanced moves###
    'moves':{
        'default':{
            'move1':{
                'name':'Full Plate And Packing Steel',
                'description':'''You ignore the clumsy tag on armor you wear''',
            },
            'move2':{
                'name':'Unencumbered',
                'description':'''So long as you are below your Load and neither wear armor nor carry a shield, take +1 armor.'''
            },
        },
        'level1':{
            'move1':{
                'name':'The Upper Hand',
                'description':'''You take +1 ongoing to last breath rolls.  When you take your last breath, on a 7–9 you make an offer to Death in return for your life. If Death accepts he will return you to life. If not, you die.'''
            },
            'move2':{
                'name':'What Are You Waiting For?',
                'description':'''When you cry out a challenge to your enemies, roll+Con. • On a 10+ they treat you as the most obvious threat to be dealt with and ignore your companions, take +2 damage ongoing against them. •On a 7–9 only a few (the weakest or most foolhardy among them) fall prey to your taunting.'''
            },
            'move3':{
                'name':'Herculean Appetites',
                'description':'''Others may content themselves with just a taste of wine, or dominion over a servant or two, but you want more. Choose two appetites. While pursuing one of your appetites if you would roll for a move, instead of rolling 2d6 you roll 1d6+1d8. If the d6 is the higher die of the pair, the GM will also introduce a complication or danger that comes about due to your heedless pursuits.''',
                'special':[
                    'Pure desctruction',
                    'Power over other',
                    'Mortal pleasures',
                    'Conquest',
                    'Riches and property',
                    'Fame and glory'
                ]
            },
            'move4':{
                'name':'Musclebound',
                'description':'''While you wield a weapon it gains the forceful and messy tags.'''
            }
        },
        'level2':{
            'move1':{
                'name':'Still Hungry',
                'description':'''Choose an additional appetite.'''
            },
            'move2':{
                'name':'Appetite for Desctruction',
                'description':'''Take a move from the Fighter, Bard, or Thief class list. You may not take multiclass moves from those classes.'''
            },
            'move3':{
                'name':'My Love For You Is Like A Truck',
                'description':'''Take a move from the Fighter, Bard, or Thief class list. You may not take multiclass\ moves from those classes.'''
            },
            'move4':{
                'name':'What Is Best In Life',
                'description':'''At the end of a session, if during this session you have crushed your enemies, seen them driven before you, or have heard the lamentations of their kinfolk mark XP.'''
            },
            'move5':{
                'name':'Wide-Wanderer',
                'description':'''You’ve travelled the wide world over. When you arrive someplace ask the GM about any important traditions, rituals, and so on, they’ll tell you what you need to know.'''
            },
            'move6':{
                'name':'Usurper',
                'description':'''When you prove yourself superior to a person in power, take +1 forward with their followers, underlings, and hangers on.'''
            },
            'move7':{
                'name':'Khan of Khans',
                'description':'''Your hirelings always accept the gratuitous fulfillment of one of your appetites as payment.'''
            },
            'move8':{
                'name':'Samson',
                'description':'''You may take a debility to immediately break free of any physical or mental restraint.'''
            },
            'move9':{
                'name':'Smash!',
                'description':'''You may take a debility to immediately break free of any physical or mental restraint.'''
            },
            'move10':{
                'name':'Indestructible Hunger',
                'description':'''When you take damage you can choose to take -1 ongoing until you sate one of your appetites instead of taking the damage. If you already have this penalty you cannot choose this option.'''
            },
            'move11':{
                'name':'Eye For Weakness',
                'description':'''When you take damage you can choose to take -1 ongoing until you sate one of your appetites instead of taking the damage. If you already have this penalty you cannot choose this option.'''
            },
            'move12':{
                'name':'On The Move',
                'description':'''When you defy a danger caused by movement (maybe falling off a narrow bridge or rushing past an armed guard) take +1.'''
            },
        },
        'level6':{
            'move1':{
                'name':'A Good Day To Die',
                'description':'''As long as you have less than your CON in current HP (or 1, whichever is higher) take +1 ongoing.'''
            },
            'move2':{
                'name':'''Kill 'Em All''',
                'description':'''Take another move fromt he Fighter, Bard, or Thief class list. You may not take multiclass moves from those classes.'''
                'requirement':'''Requires: Appetite for Destruction'''
            },
            'move3':{
                'name':'War Cry',
                'description':'''When you enter the battle with a show of force, roll +CHA. • On a 10+ both, • on a 7-9 one or the other.''',
                'special':[
                    'Your allies are rallied and take +1 forward',
                    'Your enemies feel fear and act accordingly (avoiding you, hiding, attacking with fear-driven abandon)'
                ]
            },
            'move4':{
                'name':'Mark Of Might',
                'description':'''When you take this move and spend some uninterrupted time reflecting on your past glories, you may mark yourself with a symbol of your power (a long braid tied with bells, ritual scars or tattoos, etc.) Any intelligent mortal creature who sees this symbol knows instinctively that you are a force to be reckoned with and treats you appropriately.'''
            },
            'move5':{
                'name':'More! Always More!',
                'description':'''When you satisfy an appetite to the extreme (destroying something unique and significant, gaining enormous fame, riches, power, etc.) you may choose to resolve it. Cross it off the list and mark XP. While you may pursue that appetite again, you no longer feel the burning desire you once did. In its place, choose a new appetite from the list or write your own.'''
            },
            'move6':{
                'name':'The One Who Knocks',
                'description':'''When you Defy Danger, on a 12+ you turn the danger back on itself, the GM will describe how.'''
            },
            'move7':{
                'name':'Healthy Distrust',
                'description':'''Whenever the unclean magic wielded by mortal men causes you to Defy Danger, treat any result of 6- as a 7–9.'''
            },
            'move8':{
                'name':'For The Blood God',
                'description':'''You are initiated in the old ways, the ways of sacrifice. Choose something your gods (or the ancestor spirits, or your totem, etc) value—gold, blood, bones or the like. When you sacrifice those things as per your rites and rituals, roll+WIS. • On a 10+ the GM will grant you insight into your current trouble or a boon to help you. • On a 7-9 the sacrifice is not enough and your gods take of your flesh as well, but still grant you some insight or boon. • On a miss, you earn the ire of the fickle spirits.'''
            }
        }
    }
    
}