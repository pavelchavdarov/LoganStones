
 
class Board (object):		
	#! специфично для куб-коодинат
	directions = tuple([(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0)])
	
	@staticmethod
	def get_neighbours(p_position): # (x, y, z)
		neighbours = set()
		for i in range(len(Board.directions)):
			# надо бобавить проверку на лостижение границы поля, width & high 
			_x = p_position[0] + Board.directions[i][0]
			_y = p_position[1] + Board.directions[i][1]
			_z = p_position[2] + Board.directions[i][2]
			neighbours.add((_x,_y,_z))
		return neighbours
	
	@staticmethod
	def check_position(p_position):
		if p_position[0]+p_position[1]+p_position[2]!=0:
			result = 1 # ошибка: сумма координат должна быть равна 0
		else:
			result = 0 # позиция задана корректно
		return result
	
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
			
