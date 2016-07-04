'''
Created on 2 июля 2016 г.

@author: Павел
'''
from builtins import staticmethod

class Gem(object):
    '''
    Класс описывает фишку ("камень").
    У камня есть 2 стороны с разными метками.
    На множество меток определены следующие отношения:
    - равенство (метка равна сама себе): для a из M a = a
    - превосходство: для a,b из M истинно одно из: a > b или b > a 
    '''
    
    def __init__(self, p_side_a, p_side_b):
        self.stone_sides = (p_side_a, p_side_b)
        self.currrent_side = 0
    
    def flip(self):
        self.currrent_side = (self.currrent_side + 1)%2 # 0->1, 1->0


class GemEntity:
    # надо в будущем сделать возможность задавать кол-во (3/5/7/...) сущностей
    # 0 - камень, 1 - ножницы, 2 - бумага
    
    #генерируем список сущностей и отношения между ними
    @staticmethod
    def init_entities(p_count):
        GemEntity.entity_count = p_count
        GemEntity.entities_list = [x for x in range(GemEntity.entity_count)]
        # генерируем список отношений
        GemEntity.relations = {}
        for i in GemEntity.entities_list:
            flip_list = [] # список сущсностей, которых "бьет" сущность i
            for j in range(1,GemEntity.entity_count//2+1): # кол-во сущностей = половина без i-й: если 3 сущности -- то (3-1)/2=1; если 5 -- (5-1)/2=2
                flip_list.append((i+j)%GemEntity.entity_count)
            GemEntity.relations[i] = flip_list
    
    @staticmethod
    def check_flip(entity_forcer, entity_to_flip):
        if entity_forcer in GemEntity.entities_list:
            if entity_to_flip in GemEntity.relations[entity_forcer]:
                return True
        return False
    
    
            
    

            
        