'''
Created on 5 июля 2016 г.

@author: Павел
'''
from LoganStonesGame.Entity import GemEntity
from LoganStonesGame.Gem import Gem
from _socket import SHUT_RD
from random import shuffle
from random import choice



class Pouch(object):
    '''
    classdocs
    '''

    STONE_COUNT = 18
    ENTITY_COUNT = 3

    def __init__(self):
        '''
        Constructor
        '''
        self.gems = []
        self.stone_count = Pouch.STONE_COUNT
        GemEntity.init_entities(Pouch.ENTITY_COUNT)
        for i in range(Pouch.STONE_COUNT/Pouch.ENTITY_COUNT):
            for ent in GemEntity.get_entities():
                self.gems.append(Gem(ent, GemEntity.get_entity_relation(ent)[0]))
    
    def p_shuffle(self):
        shuffle(self.gems)
    
    def f_pull_out_gem(self):
        l_gem = choice(self.gems)
        self.gems.remove(l_gem)
        return l_gem
    
    def f_gems_inside(self):
        return self.gems.__len__() 
        