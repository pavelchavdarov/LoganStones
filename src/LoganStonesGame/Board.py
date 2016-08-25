class Cell_Position (object):
	# для кубических координат
	#! специфично для куб-коодинат
	directions = tuple([(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0)])

	# применяется только для фишек на поле (доске)
	#! специфично для куб-коодинат
	def check_position(self, position):
		if position[0]+position[1]+position[2]!=0:
			result = 1 # ошибка: сумма координат должна быть равна 0
		else:
			result = 0 # позиция задана корректно
		return result
	
	#возвращает множество координат соседей
	def get_neighbours(self):
		neighbours = set()
		for i in range(len(Cell_Position.directions)):
			_x = self.X + Cell_Position.directions[i][0]
			_y = self.Y + Cell_Position.directions[i][1]
			_z = self.Z + Cell_Position.directions[i][2]
			neighbours.add((_x,_y,_z))
		return set(neighbours)

#############################################
#все правила постановки фишек, проверку достижения цели (4 в ряд) будет делать "игровая доска" 
class Board (Cell_Position):		
	
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
	
	def place_gem_on_board(self, p_gem, p_position):
		self.gems[p_position] = p_gem
			
