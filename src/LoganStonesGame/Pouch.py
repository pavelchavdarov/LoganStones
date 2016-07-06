'''
Created on 5 июля 2016 г.

@author: Павел
'''
from LoganStonesGame.Entity import GemEntity
from LoganStonesGame.Gem import Gem



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
        self.stones = []
        self.stone_count = Pouch.STONE_COUNT
        GemEntity.init_entities(Pouch.ENTITY_COUNT)
        for i in range(Pouch.STONE_COUNT/Pouch.ENTITY_COUNT):
            for ent in GemEntity.get_entities():
                self.stones.append(Gem(ent, GemEntity.get_entity_relation(ent)[0]))