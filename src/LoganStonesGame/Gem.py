'''
Created on 2 июля 2016 г.

@author: Павел
'''

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
    entities_list = [0,1,2]
    relations = {0:[1], 1:[2], 2:[0]}
    @staticmethod
    def entites_relation(p_entity_1, p_entity_2):
        if p_entity_1 == 0:
            
        