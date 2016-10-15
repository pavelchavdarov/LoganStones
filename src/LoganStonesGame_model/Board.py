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
class Board_cube (object):		
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
		return 1
		
	def place_rule(self, p_position):
		l_pos = p_position
		return 1 if l_pos[0]+l_pos[1]+l_pos[2]==0 else 0

	
	def adding_rule(self, p_position):
		neihgbours = set() ## множество соседей позиии p_position
		for d in self.directions:
			neihgbours.add((p_position[0]+d[0],p_position[1]+d[1], p_position[2]+d[2]))
		l_intersection = neihgbours.intersection()(set(self.gems))
		if len(l_intersection) >=2: # должно быть мин. 2 соседа
			return 1
		else:
			return 0 
	
	def flip_rule(self):
		return 0
	
	def place_gem_on_board(self, p_gem, p_position):
		self.gems[p_position] = p_gem
		
	def flip_gem(self,p_position):
		self.gems[p_position].flip()
			
