import random
import pygame
import settings

MOVE_UP = [0,-1]
MOVE_DOWN = [0,1]
MOVE_LEFT = [-1,0]
MOVE_RIGHT = [1,0]

class Hamiltonian_Maze:
    def __init__(self, width, height, cell_size, screen):
        self.rows = height 
        self.columns = width
        self.cell_size = cell_size
        self.screen = screen
        self.color = (255, 255, 255)
        self.prim_rows = self.rows // 2
        self.prim_cols = self.columns // 2 
        self.directions = self.prim_maze()
        self.hamiltonian_path = self.hamiltonian_cycle(self.directions)
        self.maze = self.path_generator(self.hamiltonian_path)
        self.inverted_maze = self.inverted_path(self.maze)
        # self.generate_maze()
        
        
    def display_all(self):

        for key in self.directions:
            for value in self.directions[key]:
                color = (0,0,255)
                start_point = (key[0]*self.cell_size*2 + self.cell_size, key[1]*self.cell_size*2 + self.cell_size)
                end_point = ((key[0]+ value[0])*self.cell_size*2 + self.cell_size, (key[1]+ value[1])*self.cell_size*2 + self.cell_size)
                pygame.draw.line(self.screen, color, start_point, end_point, width=3)
                
        for key in self.hamiltonian_path:
            for value in self.hamiltonian_path[key]:
                color = (255, 0, 0)
                if len(self.hamiltonian_path[key]) > 1:
                    color = (0,255,0)
                start_point = (key[0]*self.cell_size + self.cell_size//2, key[1]*self.cell_size + self.cell_size//2)
                end_point = ((0+ value[0])*self.cell_size + self.cell_size//2, (0+ value[1])*self.cell_size + self.cell_size//2)
                pygame.draw.line(self.screen, color, start_point, end_point, width=1)
                
        for i in range(self.columns//2):
            start_point = (i*settings.cell_size*2,0)
            end_point = (i * settings.cell_size*2, settings.window_size[0]-1)
            pygame.draw.line(self.screen, self.color, start_point, end_point)
        
        for i in range(self.rows//2):
            start_point = (0, i*settings.cell_size*2)
            end_point = (settings.window_size[1]-1,i * settings.cell_size*2 )
            pygame.draw.line(self.screen, self.color, start_point, end_point)
            
    def display_path(self):
        for i in range(len(self.maze)):
            pygame.draw.line(self.screen, self.color, (self.maze[i-1][0] * self.cell_size + self.cell_size //2, self.maze[i-1][1] * self.cell_size + self.cell_size //2),
                             (self.maze[i][0] * self.cell_size + self.cell_size //2, self.maze[i][1] * self.cell_size + self.cell_size //2), width=2)
                
    def generate_maze(self):
        print(self.directions)
        print(self.hamiltonian_path)
        print(self.maze)
        
        
    def display_dict(self, directions):
        for key in directions:
            
            for value in directions[key]:
                color = (255,0,0)
                start_point = (key[0], key[1])
                end_point = ((key[0]+ value[0]), (key[1]+ value[1]))
                print(start_point, end_point)
        
    def prim_maze(self):
        directions = dict()
        vertices = self.prim_rows * self.prim_cols
        
        for i in range(self.prim_rows):
            for j in range(self.prim_cols):
                directions[j, i] = []
        print(self.prim_cols-1, self.prim_rows)
        x = random.randint(0, self.prim_cols - 1)
        y = random.randint(0, self.prim_rows - 1)
        initial_cell = (x, y)
         
        current_cell = initial_cell
        visited = [(x, y)]
        
        adjacent_cells = set()
        while len(visited) != vertices:
            
            x_position = current_cell[0]
            y_position = current_cell[1]
            
            # if the current cell is not on any type of edge
            if x_position != 0 and y_position != 0 and x_position != self.prim_cols -1 and y_position != self.prim_rows - 1:
                adjacent_cells.add((x_position, y_position - 1))
                adjacent_cells.add((x_position, y_position + 1))
                adjacent_cells.add((x_position - 1, y_position))
                adjacent_cells.add((x_position + 1, y_position))
            
            # if the current cell is top-left corner
            elif x_position == 0 and y_position == 0: 
                adjacent_cells.add((x_position + 1, y_position))
                adjacent_cells.add((x_position, y_position + 1))
            
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
            elif  x_position == self.prim_cols -1 and y_position == 0:
                adjacent_cells.add((x_position, y_position + 1))
                adjacent_cells.add((x_position - 1, y_position))
                
            # if the current cell in bottom right corner of the grid
            elif x_position == self.prim_cols -1 and y_position == self.prim_rows -1:
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
                adjacent_cells.add((x_position, y_position - 1))
                adjacent_cells.add((x_position + 1, y_position))
                adjacent_cells.add((x_position - 1, y_position))
                
            while current_cell:
                # choose a random current cell

                current_cell = random.choice(tuple(adjacent_cells))
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
                
        # return self.hamiltonian_cycle(directions)
        return directions
    
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
                        hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 1, i*2 + 2)]
                    else:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_RIGHT not in directions[j - 1, i]:
                        hamiltonian_graph[j*2, i*2] += [(j*2, i*2 + 1)]
                        
                # if the adjacent cells lie in the right column
                elif j == self.prim_cols - 1: 
                    hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_DOWN in directions[j,i]:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2 , i*2 + 2)]
                        hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 1, i*2 + 2)]
                    else:
                        hamiltonian_graph[j*2 , i*2 + 1] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_DOWN not in directions[j, i-1]:
                        hamiltonian_graph[j*2, i*2] = [(j*2 + 1, i*2)]
                    if MOVE_RIGHT not in directions[j-1, i]:
                        if (j*2, i*2) in hamiltonian_graph:
                            hamiltonian_graph[j * 2, i *2] += [(j *2, i * 2 + 1 )]
                        else:
                            hamiltonian_graph[j * 2, i * 2] = [(j*2, i *2 + 1)]
                
                # if the adjacent cells lie in the top left corner
                elif j == 0 and i == 0:
                    hamiltonian_graph[j*2, i*2] = [(j*2 + 1, i*2)]
                    hamiltonian_graph[j*2, i*2] += [(j*2, i*2 + 1)]
                    if MOVE_RIGHT in directions[j, i]:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 2, i*2)]
                        hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 2, i*2 + 1)]
                    else:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_DOWN in directions[j, i]:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2, i*2 + 2)]
                        if (j*2 + 1, i*2 + 1) in hamiltonian_graph:
                            hamiltonian_graph[j * 2 + 1, i * 2 + 1] += [(j * 2 + 1, i * 2 + 2)]
                        else:
                            hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 1, i*2 + 2)]
                    else:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2 + 1, i*2 + 1)]
                
                # if the adjacent cells lie bottom left corner
                elif j == 0 and i == self.prim_rows - 1:
                    hamiltonian_graph[j*2, i*2] = [(j*2, i*2 + 1)]
                    hamiltonian_graph[j*2, i*2+1] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_RIGHT in directions[j,i]:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 2, i*2)]
                        hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 2, i*2 + 1)]
                    else:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_DOWN not in directions[j, i -1]:
                        hamiltonian_graph[j*2, i*2] +=  [(j*2 + 1, i*2)]
                        
                # if the adjacent cells lie in the left column
                elif j == 0:
                    hamiltonian_graph[j*2, i*2] = [(j*2, i*2 + 1)]
                    if MOVE_RIGHT in directions[j, i]:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 2, i*2)]
                        hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 2, i*2 + 1)]
                    else:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_DOWN in directions[j, i]:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2, i*2 + 2)]
                        if (j*2 + 1, i*2 + 1) in hamiltonian_graph:
                            hamiltonian_graph[j*2 + 1, i*2 + 1] += [(j*2 + 1, i*2 + 2)]
                        else:
                            hamiltonian_graph[j * 2 + 1, i * 2 + 1] = [(j * 2 + 1, i * 2 + 2)]
                    else:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_DOWN not in directions[j, i-1]:
                        hamiltonian_graph[j*2, i*2] += [(j*2 + 1, i*2)]
                        
                # if the adjacent cells lie in the top row
                elif i == 0:
                    hamiltonian_graph[j*2, i*2] = [(j*2 + 1, i*2)]
                    if MOVE_RIGHT in directions[j, i]:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 2, i*2)]
                        hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 2, i*2 + 1)]
                    else:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 1, i*2 + 1)]
                    if  MOVE_DOWN in directions[j, i]:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2, i*2 + 2)]
                        if (j*2 + 1, i*2 + 1) in hamiltonian_graph:
                            hamiltonian_graph[j * 2 + 1, i * 2 + 1] += [(j * 2 + 1, i * 2 + 2)]
                        else:
                            hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 1, i*2 + 2)]
                    else:
                        hamiltonian_graph[j*2, i*2 + 1] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_RIGHT not in directions[j-1, i]:
                        hamiltonian_graph[j*2, i*2] += [(j*2, i*2 + 1)]
                     
                else:
                    hamiltonian_graph[j*2, i*2 + 1] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_RIGHT in directions[j, i]:
                        hamiltonian_graph[j*2 + 1, i*2 + 1] = [(j*2 + 2, i*2 + 1)]
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 2, i*2)]
                    else:
                        hamiltonian_graph[j*2 + 1, i*2] = [(j*2 + 1, i*2 + 1)]
                    if MOVE_DOWN in directions[j, i-1]:
                        hamiltonian_graph[j*2, i*2] = [(j*2 + 1, i*2)]
                    if MOVE_DOWN not in directions[j-1, i]:
                        if (j*2, i*2) in hamiltonian_graph:
                            hamiltonian_graph[j*2, i*2] += [(j*2, i*2 + 1)]
                        else:
                            hamiltonian_graph[j * 2, i * 2] = [(j * 2, i * 2 + 1)]
        # return self.path_generator(hamiltonian_graph)
        return hamiltonian_graph
    
    def path_generator(self, graph):
        cells =  self.prim_cols*self.prim_rows*4
        path = [(0,0)]
        previous_cell = path[0]
        previous_direction = None
         
         # generates a path that is a hamiltonian cycle by following a set of general laws
         #1. If the right cell is available, travel right
         #2. if the cell under ir availeble,travel down
         #3. if the left cell is available, travel left
         #4. If the cell above is available, travel up
         #5. The current direction cannot oppose the previous direction 
         # eg left cannot be present after right since it is opposed
        while len(path) != cells:
             
            if previous_cell in graph and (previous_cell[0] + 1, previous_cell[1]) in graph[previous_cell] and previous_direction != MOVE_LEFT:
                next_cell = (previous_cell[0] + 1, previous_cell[1])
                previous_direction = MOVE_RIGHT
                extra_cell = [next_cell[0], next_cell[1]]
                path.append(extra_cell)
                previous_cell = next_cell
            elif previous_cell in graph and (previous_cell[0], previous_cell[1] + 1) in graph[previous_cell] and previous_direction != MOVE_UP:
                next_cell = (previous_cell[0], previous_cell[1] + 1)
                previous_direction = MOVE_DOWN
                extra_cell = [next_cell[0], next_cell[1]]
                path.append(extra_cell)
                previous_cell = next_cell
            elif (previous_cell[0] - 1, previous_cell[1]) in graph and previous_cell in graph[previous_cell[0] - 1, previous_cell[1]] and previous_direction != MOVE_RIGHT:
                next_cell = (previous_cell[0] - 1, previous_cell[1])
                previous_direction = MOVE_LEFT
                extra_cell = [next_cell[0], next_cell[1]]
                path.append(extra_cell)
                previous_cell = next_cell
            else:
                next_cell = (previous_cell[0], previous_cell[1] - 1)
                previous_direction = MOVE_UP
                extra_cell = [next_cell[0], next_cell[1]]
                path.append(extra_cell)
                previous_cell = next_cell
                
        path[0]= [0,0]
        # print(path)
        self.inverted_path(path)
        return path
    
    def inverted_path(self, path):
        inverted_path = [[0 for _ in range(self.rows)] for _ in range(self.columns)]
        for i, location in enumerate(path):
            inverted_path[location[0]][location[1]] = i
            
        return inverted_path
            

