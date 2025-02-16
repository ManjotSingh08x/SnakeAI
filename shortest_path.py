from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.heuristic import manhattan


class ShortestPath:
    def __init__(self, screen, rows, columns):
        self.finder = AStarFinder(heuristic=manhattan)
        self.screen = screen
        self.rows = rows
        self.columns = columns
        
    def create_grid(self, snake_arr, food_pos):
        path_grid = []
        for i in range(self.columns):
            arr = []
            for j in range(self.rows):
                arr.append(1)
            path_grid.append(arr)
        for segment in snake_arr[1:]:
            x = segment[0]
            y = segment[1]
            # print(segment)
            path_grid[y][x] = 0
        return path_grid
    
    def calculate_path(self, snake_arr, food_pos):
        path_grid = self.create_grid(snake_arr, food_pos)
        grid = Grid(matrix=path_grid)
        start = grid.node(snake_arr[0][0], snake_arr[0][1])
        end = grid.node(food_pos[0], food_pos[1])
        path, runs = self.finder.find_path(start=start, end=end, graph=grid)
        # print(grid.grid_str(path,start,end,border=True))
        return path