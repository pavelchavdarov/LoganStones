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
    GEM_SIDES = 2 # always 2 sides, because of relation "A beats B" 
    def __init__(self, p_side_a, p_side_b):
        self.stone_sides = (p_side_a, p_side_b)
        self.currrent_side = 0
    
    def flip(self):
        self.currrent_side = (self.currrent_side + 1)%2 # 0->1, 1->0
    
    def current_side(self):
        return self.stone_sides[self.currrent_side]

    
    
            
    

            
        