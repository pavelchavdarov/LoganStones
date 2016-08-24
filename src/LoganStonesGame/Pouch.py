'''
Created on 5 июля 2016 г.

@author: Павел
'''
from LoganStonesGame.Entity import GemEntity
from LoganStonesGame.Gem import Gem
from random import shuffle
from random import choice
import math



class Pouch(object):
    '''
    classdocs
    '''

    #STONE_COUNT = 18
    ENTITY_COUNT = 3
    #GEMS_PER_PLAYER = 8
    GEM_COMBOS_AMOUNT = 6

    def __comb__(self, entity_amount, set_size):
        return math.factorial(entity_amount)/(math.factorial(set_size)*math.factorial(entity_amount - set_size))
    
    def __init__(self):
        '''
        Constructor
        '''
        self.stone_count = (Pouch.GEMS_PER_PLAYER + 1)*2; # 2 players. every player puts 1 gem on the board at start of a game
        self.gems = []
        GemEntity.init_entities(Pouch.ENTITY_COUNT)
        gem_combinations = Pouch.__comb__(Pouch.ENTITY_COUNT,Gem.GEM_SIDES)
        self.stone_count = gem_combinations * Pouch.GEM_COMBOS_AMOUNT
        for i in range(Pouch.GEM_COMBOS_AMOUNT): # 
            # generation of unique pairs of entities
            for ent in GemEntity.get_entities():
                for gem_rel in GemEntity.get_entity_relation(ent):
                    self.gems.append(Gem(ent, gem_rel))
    
    def p_shuffle(self):
        shuffle(self.gems)
    
    def f_pull_out_gem(self):
        l_gem = choice(self.gems)
        self.gems.remove(l_gem)
        return l_gem
    
    def f_gems_inside(self):
        return self.gems.__len__() 
        