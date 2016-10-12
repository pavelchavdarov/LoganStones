'''
Created on 26 авг. 2016 г.

@author: PChavdarov
'''

def place_rool(func):
        def position_checker(*args, **kwargs):
            # проверка
            l_pos = args[2] # первым аргументов ожидаем координаты
            if l_pos[0]+l_pos[1]+l_pos[2]==0:
                func(*args, **kwargs)
            #else:
            #    Exception()
        
        return position_checker
