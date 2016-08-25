class Cell_Position (object):
	# для кубических координат
	#! специфично для куб-коодинат
	directions = tuple([(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0)])

# убрать это отсюда. признаков не будет. Объекты фишек буду переноситься из одного списка в другой: из списка "мешочек" в список "игров_1", от туда в список "доска"
################################	
#	# x==y==z==-1 --- значит фишка в мешочке
#	#! специфично для куб-коодинат
#	def into_baggie(self):
#		self.X = -1
#		self.Y = -1
#		self.Z = -1
#	# x==y==z==N and N>0 --- значит фишка у игрока N
#	#! специфично для куб-коодинат
#	def to_player(self, player_num):
#		self.X = player_num
#		self.Y = player_num
#		self.Z = player_num
################################

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
	def island_rule(self):
		return 0
		
	def adding_rule(self):
		return 0 # ту нужно реализовать проверку соседей: должно быть мин. 2 соседа
	
	def place_on_board(self, position):
		# проверка позиции на доске
		None
			
