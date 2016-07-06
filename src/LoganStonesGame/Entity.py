'''
Created on 5 июля 2016 г.

@author: Павел
'''
class GemEntity:
    # надо в будущем сделать возможность задавать кол-во (3/5/7/...) сущностей
    # 0 - камень, 1 - ножницы, 2 - бумага
    GemEntity.relations = {}
    #генерируем список сущностей и отношения между ними
    @staticmethod
    def init_entities(p_count):
        GemEntity.entity_count = p_count
        GemEntity.entities_list = [x for x in range(GemEntity.entity_count)]
        #GemEntity.entities_list = ["Камень","Ножницы","Бумага"]
        # генерируем список отношений
        GemEntity.relations = {}
        for i in range(GemEntity.entity_count):
            flip_list = [] # список сущсностей, которых "бьет" сущность i
            for j in range(1,GemEntity.entity_count//2+1): # кол-во сущностей = половина без i-й: если 3 сущности -- то (3-1)/2=1; если 5 -- (5-1)/2=2
                flip_list.append( GemEntity.entities_list[(i+j)%GemEntity.entity_count] )
            GemEntity.relations[GemEntity.entities_list[i]] = flip_list
    
    @staticmethod
    def check_flip(entity_forcer, entity_to_flip):
        if entity_forcer in GemEntity.entities_list:
            if entity_to_flip in GemEntity.relations[entity_forcer]:
                return True
        return False
    
    @staticmethod
    def get_entity_relation(entity):
        if entity in GemEntity.entities_list:
            return GemEntity.relations[entity]
        else:
            return {}
    
    @staticmethod
    def get_entities():
        return GemEntity.entities_list