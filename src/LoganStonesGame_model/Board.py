from _functools import reduce
from LoganStonesGame_model.Entity import GemEntity
from random import randrange


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
		return set(tuple(map(lambda x,y:x+y, tuple(p_position), z)) for z in self.directions)
		
	def __init__(self, gem_1=None, gem_2 = None):
		self.gems = dict() # камни на доске
		if gem_1 and gem_2:
			self.gems[(0,0,0)] = gem_1
			l_pos = randrange(0,6)
			self.gems[self.directions[l_pos]] = gem_2

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
				#print('adding_rule - yes')
				self.gems[tuple(p_position)] = p_gem
				for gem_pos in list(filter(lambda x: GemEntity.check_flip(p_gem.get_current_side(), self.gems[x].get_current_side()), adding['neighbors'])):
					#print('flipping')
					self.flip_gem(gem_pos)
				return 0
			else:
				return 1
				
	def flip_gem(self,p_position):
		self.gems[tuple(p_position)].flip()
			
