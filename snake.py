import pygame
import settings

CELL_SIZE = settings.cell_size
WINDOW_SIZE = settings.window_size
RED = (200 , 0 , 0)
GREEN = (0 , 160 , 0)

MOVE_UP = [0,-1]
MOVE_DOWN = [0,1]
MOVE_LEFT = [-1,0]
MOVE_RIGHT = [1,0]

P = 1

VEL = 10

class Snake:
    def __init__(self , arr):
        self.arr = arr
        self.length = len(self.arr)
        self.head_x = self.arr[0][0]
        self.head_y = self.arr[0][1]
        self.dir = MOVE_UP
        self.ticks = 0
        self.velocity = VEL

    def draw(self , screen):
        for i , section in enumerate(self.arr):
            pygame.draw.rect(screen , GREEN , (section[0]*CELL_SIZE+P , section[1]*CELL_SIZE+P , CELL_SIZE-2*P , CELL_SIZE-2*P ))
            if i>0 and i < self.length-1:
                offset_x1 = self.arr[i-1][0] - self.arr[i][0]
                offset_x2 = self.arr[i+1][0] - self.arr[i][0]
                offset_y1 = self.arr[i-1][1] - self.arr[i][1]
                offset_y2 = self.arr[i+1][1] - self.arr[i][1]
                if abs(offset_x1) < 2 and abs(offset_x2) < 2 and abs(offset_y1) < 2 and abs(offset_y2) < 2:
                    pygame.draw.rect(screen , GREEN , (section[0]*CELL_SIZE+P+offset_x1*P , section[1]*CELL_SIZE+P+offset_y1*P , CELL_SIZE-2*P , CELL_SIZE-2*P ))
                    pygame.draw.rect(screen , GREEN , (section[0]*CELL_SIZE+P+offset_x2*P , section[1]*CELL_SIZE+P+offset_y2*P , CELL_SIZE-2*P , CELL_SIZE-2*P ))
            elif i==0:
                offset_x2 = self.arr[i+1][0] - self.arr[i][0]
                offset_y2 = self.arr[i+1][1] - self.arr[i][1]
                if abs(offset_y2) < 2 and abs(offset_x2) < 2:
                    pygame.draw.rect(screen , GREEN , (section[0]*CELL_SIZE+P+offset_x2*P , section[1]*CELL_SIZE+P+offset_y2*P , CELL_SIZE-2*P , CELL_SIZE-2*P ))
            else:
                offset_x1 = self.arr[i-1][0] - self.arr[i][0]
                offset_y1 = self.arr[i-1][1] - self.arr[i][1]
                if abs(offset_y1) < 2 and abs(offset_x1) < 2:
                    pygame.draw.rect(screen , GREEN , (section[0]*CELL_SIZE+P+offset_x1*P , section[1]*CELL_SIZE+P+offset_y1*P , CELL_SIZE-2*P , CELL_SIZE-2*P ))



    def move(self):
        self.ticks +=1
        if self.ticks > self.velocity:
            for i in range(self.length-1 ,0, -1):
                if i:
                    self.arr[i][0] = self.arr[i-1][0]
                    self.arr[i][1] = self.arr[i-1][1]
            self.arr[0] = self.future_head()
            self.ticks = 0
            # print(self.arr)

    def future_head(self):
        naive_future = [self.arr[0][0] + self.dir[0] , self.arr[0][1]+self.dir[1]]
        if naive_future[0]*CELL_SIZE >= WINDOW_SIZE[0]:
            naive_future[0] -= WINDOW_SIZE[0]//CELL_SIZE 
        if naive_future[1]*CELL_SIZE >= WINDOW_SIZE[1]:
            naive_future[1] -= WINDOW_SIZE[1]//CELL_SIZE
        if naive_future[0] < 0:
            naive_future[0] += WINDOW_SIZE[0]//CELL_SIZE
        if naive_future[1] < 0:
            naive_future[1] += WINDOW_SIZE[1]//CELL_SIZE
        return naive_future
