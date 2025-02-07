import random

MOVE_UP = [0,-1]
MOVE_DOWN = [0,1]
MOVE_LEFT = [-1,0]
MOVE_RIGHT = [1,0]

class Hamiltonian_Maze:
    def __init__(self, height, width):
        self.rows = height 
        self.columns = width
        self.prim_rows = self.rows // 2
        self.prim_cols = self.columns // 2 
        
    def prim_maze(self):
        directions = dict()
        vertices = self.prim_rows * self.prim_cols
        
        for i in range(self.prim_rows):
            for j in range(self.prim_cols):
                directions[j, i] = []
                
        x = randint(0, self.prim_cols - 1)
        y = randint(0, self.prim_rows - 1)
        initial_cell = (x, y)
         
        current_cell = initial_cell
        visited = [initial_cell]
        
        adjacent_cells = set()
        while len(visited) != vertices:
            
            x_position = current_cell[0]
            y_position = current_cell[1]
            
            # if the current cell is not on any type of edge
            if x_position != 0 and y_position != 0 and x_position != self.prim_cols -1 and y_position != self.prim_rows:
                adjacent_cells.add((x_position, y_position - 1))
                adjacent_cells.add((x_position, y_position + 1))
                adjacent_cells.add((x_position - 1, y_position))
                adjacent_cells.add((x_position + 1, y_position))
            
            # if the current cell is top-left corner
            elif x_position == 0 and y_position == 0: 
                adjacent_cells.add((x_position, y_position + 1))
                adjacent_cells.add((x_position + 1, y_position))
            
            # if the current cell is bottom-left corner
            elif x_position == 0 and y_position == self.prim_rows -1:
                adjacent_cells.add((x_position, y_position - 1))
                adjacent_cells.add((x_position + 1, y_position))
                
            # if the current cell is left column of grid
            elif x_position == 0:
                adjacent_cells.add((x_position, y_position - 1))
                adjacent_cells.add((x_position, y_position + 1))
                adjacent_cells.add((x_position + 1, y_position))
                
            # if the current cell is top right corner of the gird
            elif  y_position == 0 and x_position == self.prim_cols -1:
                adjacent_cells.add((x_position, y_position + 1))
                adjacent_cells.add((x_position - 1, y_position))
                
            # if the current cell in bottom right corner of the grid
            elif x_position == self.prim_cols -1 and y_position == self.prim_rows:
                adjacent_cells.add((x_position, y_position - 1))
                adjacent_cells.add((x_position - 1, y_position))
                
            # if the current cell is right column of the grid
            elif x_position == self.prim_cols -1:
                adjacent_cells.add((x_position, y_position - 1))
                adjacent_cells.add((x_position, y_position + 1))
                adjacent_cells.add((x_position - 1, y_position))
                
            # if the current cell is top row of the grid
            elif y_position == 0:
                adjacent_cells.add((x_position, y_position + 1))
                adjacent_cells.add((x_position - 1, y_position))
                adjacent_cells.add((x_position + 1, y_position))
                
            else:
                adjacent_cells.add((x_position, y_position + 1))
                adjacent_cells.add((x_position - 1, y_position))
                adjacent_cells.add((x_position + 1, y_position))
                
            while current_cell:
                # choose a random current cell
                current_cell = random.sample(adjacent_cells, 1)[0]
                adjacent_cells.remove(current_cell)
                
                if current_cell not in visited:
                    
                    visited.append(current_cell)
                    x = current_cell[0]
                    y = current_cell[1]
                    
                    if (x + 1, y) in visited:
                        directions[x,y] += [MOVE_RIGHT]
                    elif (x - 1, y) in visited:
                        directions[x - 1, y] += [MOVE_RIGHT]
                    elif(x, y + 1) in visited:
                        directions[x, y] += [MOVE_DOWN]
                    elif(x, y-1) in visited:
                        directions[x,y -1] += [MOVE_DOWN]
                        
                    break
                
        return self.hamiltonian_cycle(self, directions)
    
    def hamiltonian_cycle(self, directions):
        
        hamiltonian_graph = dict()
        
        for i in range(self.prim_rows):
            for j in range(self.prim_cols):
                
                # if the adjacent cells dont lie on edges
                if j != self.prim_cols - 1 and i != self.prim_rows and j != 0 and i != 0:
                    if MOVE_RIGHT in directions[j, i]:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 2, i*2)]
                        hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 2, i*2 + 1)]
                        
                    else:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j * 2 + 1, i*2 + 1)]
                    
                    if MOVE_DOWN in directions[j, i]:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2, i*2 + 2)]
                        if (j*2 + 1, i*2 + 1) in hamiltonian_graph:
                            hamiltonian_graph[j*2 + 1, i*2 + 1] += [(j*2 + 1, i * 2 + 2)]
                        else:
                            hamiltonian_graph[j*2 + 1, i * 2 + 1] = [(j * 2 + 1, i * 2 + 2)]
                    else:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2 + 1, i * 2 + 1)]
                        
                    if MOVE_DOWN not in directions[j, i -1]:
                        hamiltonian_graph[j * 2, i *2 ] = [(j*2 + 1, i * 2)]
                    if MOVE_RIGHT not in directions[j - 1, i]:
                        if (j*2, i*2) in hamiltonian_graph:
                            hamiltonian_graph[j*2, i * 2] += [(j * 2, i * 2 + 1)]
                        else:
                            hamiltonian_graph[j * 2, i * 2] = [(j * 2, i * 2 + 1)]
                            
                # if the adjacent cells lie on the bottom right corner
                elif j == self.prim_cols - 1 and  i == self.prim_rows - 1: 
                    hamiltonian_graph[j*2, i*2 + 1] = [(j*2 + 1, i *2 + 1)]
                    hamiltonian_graph[j*2  + 1, i*2] = [(j*2 +1, i*2 + 1)]
                    if MOVE_DOWN not in directions[j, i -1]:
                        hamiltonian_graph[j*2, i*2] = [(j*2 +1, i*2)]
                    elif MOVE_RIGHT not in directions[j-1, i]:
                        hamiltonian_graph[j*2, i*2] = [(j*2, i*2 + 1)]
                        
                # if the adjacent cells lie on the top right corner
                elif j == self.prim_cols - 1 and i == 0:
                    hamiltonian_graph[j*2, i*2] = [(j*2 + 1, i*2)]
                    hamiltonian_graph[j*2 + 1, i * 2] = [(j*2 + 1, i * 2 + 1)]
                    if MOVE_DOWN in directions[j, i]:
                        hamiltonian_graph[j*2, i * 2 + 1] = [(j*2, i*2 + 2)]
                     