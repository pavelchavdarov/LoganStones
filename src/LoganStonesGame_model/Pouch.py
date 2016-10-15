'''
Created on 5 июля 2016 г.

@author: Павел
'''
from LoganStonesGame_model.Entity import GemEntity
from LoganStonesGame_model.Gem import Gem
from random import shuffle
from random import choice
from math import factorial



class Pouch(object):
    '''
    classdocs
    '''


    ENTITY_COUNT = 3 #кол-во сущностей в игре. по умолчанию 3 -- камень, ножницы, бумага
    GEM_TYPE_INSTANTS = 6 # число дубликатов уникальных фишек
    
    @staticmethod
    def __combs__(entity_amount, set_size):
        return factorial(entity_amount)/(factorial(set_size)*factorial(entity_amount - set_size))
    
    def __init__(self):
        '''
        Constructor
        '''
        self.gems = []
        GemEntity.init_entities(Pouch.ENTITY_COUNT)
        gem_types = Pouch.__combs__(Pouch.ENTITY_COUNT, Gem.GEM_SIDES)
        self.stone_count = gem_types * Pouch.GEM_TYPE_INSTANTS
        for i in range(Pouch.GEM_TYPE_INSTANTS): # по числу дубликатов уникальных фишек
            # создание уникальных фишек: для каждой сущности создается фишка: на одной стороне текущая сущность, на другой - парная сущностью меньшего ранга
            for ent in GemEntity.get_entities():
                for gem_rel in GemEntity.get_entity_relation(ent): # получение списка сущностей меньшего ранга для сущности ent
                    self.gems.append(Gem(ent, gem_rel))
    
    def p_shuffle(self):
        shuffle(self.gems)
    
    def f_pull_out_gem(self):
        l_gem = None
        if self.f_gems_inside() >0 : 
            l_gem = choice(self.gems) # берем случайную фишку из мешочка
            self.gems.remove(l_gem) # удаляем из мешочка попавшуюся фишку
        return l_gem
    
    def f_gems_inside(self):
        return self.gems.__len__() 
        