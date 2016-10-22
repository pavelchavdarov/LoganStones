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

def neighbours_rool(func):
	def neighbours_checker(*args, **kwargs):
		neihgbours = set() ## множество соседей позиии p_position
		for d in args[0].directions:
			neihgbours.add((args[2].[0]+d[0],args[2].[1]+d[1], args[2].[2]+d[2]))
		l_intersection = neihgbours.intersection()(set(args[0].gems))
		if len(l_intersection) >=2: # должно быть мин. 2 соседа
			func(*args, **kwargs)
#		else:
#			Exception
	
	return neighbours_checker 
'''
from _functools import reduce
from LoganStonesGame_model.Entity import GemEntity

class Board_cube (object):		
	#! специфично для куб-коодинат
	directions = tuple([(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0)])
	point_move = lambda point, delta : point + delta
	
	# применяется только для фишек на поле (доске)
	#! специфично для куб-коодинат
	'''def check_position(self, position):
		if position[0]+position[1]+position[2]!=0:
			result = 1 # ошибка: сумма координат должна быть равна 0
		else:
			result = 0 # позиция задана корректно
		return result'''
	# возвращает множество из 6 соседей для p_position 
	def _get_neihgbours(self,p_position):
		return set(tuple(map(self.point_move, p_position, x)) for x in self.directions)
		
	def __init__(self):
		self.gems = dict() # камни на доске
	
	def island_rule(self):
		return 1==1
		
	def place_rule(self, p_position):
		l_pos = p_position[:]
		return reduce(lambda x, y : x+y, l_pos ) == 0

	
	def adding_rule(self, p_position):
		neighbors = self._get_neihgbours(p_position)
		l_intersection = neighbors & set(self.gems)
		return {'rule':len(l_intersection) >= 2, 'neighbors':l_intersection}# должно быть мин. 2 соседа
	
	def flip_rule(self):
		return True
	
	def place_gem_on_board(self, p_gem, p_position):
		if self.place_rule(p_position):
			adding = self.adding_rule(p_position)
			if adding['rule']:
				self.gems[p_position] = p_gem
				map(self.flip_gem,filter(lambda x: GemEntity.check_flip(p_gem.current_side, self.gems[x].current_side), adding['neighbors']))
				
		
	def flip_gem(self,p_position):
		self.gems[p_position].flip()
			
