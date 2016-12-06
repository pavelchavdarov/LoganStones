'''
Created on 5 июля 2016 г.

@author: Павел
'''

class GemEntity():
    # надо в будущем сделать возможность задавать кол-во (3/5/7/...) сущностей
    # 0 - камень, 1 - ножницы, 2 - бумага
    relations = {}
    #генерируем список сущностей и отношения между ними
    @staticmethod
    def init_entities(p_count):
        # чтобы p_count всегда было нечетным
        p_count = p_count + 1 - p_count%2
        GemEntity.entitys_amount = p_count
        GemEntity.entities_list = list()
        for i in range(p_count):
            GemEntity.create()
            
#        GemEntity.entities_list = ['Stone', 'Scissors', 'Paper']#[x for x in range(GemEntity.entitys_amount)]
        #GemEntity.entities_list = ["Камень","Ножницы","Бумага"]
        # генерируем список отношений
#        GemEntity.relations = {}
#        for i in range(GemEntity.entitys_amount):
#            flip_list = [] # список сущсностей, которых "бьет" сущность i
#            for j in range(1,GemEntity.entitys_amount//2+1): # кол-во сущностей = половина без i-й: если 3 сущности -- то (3-1)/2=1; если 5 -- (5-1)/2=2
#                flip_list.append( GemEntity.entities_list[(i+j)%GemEntity.entitys_amount] )
#            GemEntity.relations[GemEntity.entities_list[i]] = flip_list
    
    @staticmethod
    def create():
        if GemEntity.entitys_amount :
            if len(GemEntity.entities_list) <= GemEntity.entitys_amount:
                GemEntity.entities_list.add(GemEntity())
    
    def __init__(self):
        self.makr = len(GemEntity.entities_list)%GemEntity.entitys_amount # перестраховка на всякий случай
        flip_list = list()
        for j in range(1,GemEntity.entitys_amount//2+1): # кол-во сущностей = половина без i-й: если 3 сущности -- то (3-1)/2=1; если 5 -- (5-1)/2=2
            flip_list.append( (self.makr+j)%GemEntity.entitys_amount )
        self.flip_list = flip_list
    
    @staticmethod
    def check_flip(entity_forcer, entity_to_flip):
        if entity_forcer in GemEntity.entities_list:
            if entity_to_flip in GemEntity.relations[entity_forcer]:
                return True
        return False
    
    def check_to_flip(self, entity_forcer):
        if self.makr in entity_forcer.flip_list:
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
    
    @staticmethod
    def get_entities_amount():
        return GemEntity.entitys_amount