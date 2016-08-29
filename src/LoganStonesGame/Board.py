
from LoganStonesGame.GameRoolCheckers import *


 
class Board (object):		
	#! специфично для куб-коодинат
	directions = tuple([(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0)])

	# применяется только для фишек на поле (доске)
	#! специфично для куб-коодинат
	'''def check_position(self, position):
		if position[0]+position[1]+position[2]!=0:
			result = 1 # ошибка: сумма координат должна быть равна 0
		else:
			result = 0 # позиция задана корректно
		return result'''
	
	def __init__(self):
		self.gems = dict() # камни на доске
	
	def island_rule(self):
		def check_island_rule(self, gem_dict):
			None
			
		return check_island_rule
		
	def adding_rule(self):
		return 0 # тут нужно реализовать проверку соседей: должно быть мин. 2 соседа
	
	def flip_rule(self):
		return 0
	
	@place_rool
	def place_gem_on_board(self, p_gem, p_position):
		self.gems[p_position] = p_gem
		
	def flip_gem(self,p_position):
		self.gems[p_position].flip()
			
