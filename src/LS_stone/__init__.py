
class StoneSide:
    __sides__ = {'Камень', 'Ножницы', 'Бумага'}

class CellCoordinates:
    directions = [(0,1,-1), (1,0,-1), (1,-1,0), (0,-1,1), (-1,0,1), (-1,1,0)]
    
    def cell_direction(self, dir):
        return self.directions[dir]
            
    def __init__(self, p_x, p_y, p_z):
        if p_x + p_y + p_z == 0:
            self.X = p_x
            self.Y = p_y
            self.Z = p_z
        else:
            self.X = self.Y = self.Z = 0
    
    def __show__(self):
        print("X=%s Y=%s Z=%s"%(self.X, self.Y, self.Z) )
        
    def cell_set(self,p_x, p_y, p_z):
        if p_x + p_y + p_z == 0:
            self.X = p_x
            self.Y = p_y
            self.Z = p_z
    
    def cell_add(self, hex, direction):
        
        hex.X = hex.X + self.cell_direction(direction)[0] # X
        hex.Y = hex.Y + self.cell_direction(direction)[1] # Y
        hex.Z = hex.Z + self.cell_direction(direction)[2] # Z
        return hex
        
    
    def get_neighbours(self):
        neighbours = set()
        #neighbour = CellCoordinates
        for i in range(len(self.directions)):
            neighbour = self.cell_add(self, i)
            print("neighbour[%s]=%s"%(i,neighbour))
            neighbours.add(neighbour)
        return neighbours
    
class Stone:
    # 0 - side-1 = side_2, 1 - side-1 > side_2, 2 - sided_1 < side_2 
    def sides_retio(p_side_a, p_side_b):
        if p_side_a == p_side_b:
            return 0
        elif p_side_a==0:     # stone
            if p_side_b==1:       # scissors
                return 1            # stone > scissors
            elif p_side_b==2:     # paper
                return 2            # stone < paper
        elif p_side_a==1:     # scissors
            if p_side_b==0:       # stone
                return 2            # scissors < stone
            elif p_side_b==2:     # paper
                return 1            # scissors > paper
        elif p_side_a==2:     # paper
            if p_side_b==0:       # stone
                return 1            # paper > stone
            elif p_side_b==1:     # scissors
                return 2            # paper < scissors 
    
    sides_retio = staticmethod(sides_retio)
        
    def __init__(self, p_side_a, p_side_b):
        self.is_init = True
        self.Side_A = p_side_a
        self.Side_B = p_side_b
        self.Current_Side = p_side_a
    
    def flip_stone(self):
        self.Current_Side = self.Side_B if self.Current_Side == self.Side_A else self.Side_A
        
    def try_to_flip(self, force_side):
        if Stone.sides_retio(force_side, self.Current_Side) == 1:
            self.flip_stone()



    
                