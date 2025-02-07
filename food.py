import pygame
import random

CELL_SIZE = 20
WINDOW_SIZE = (800,600)
RED = (200 , 0 , 0)


class Food:
    def __init__(self , x , y):
        self.pos = [x,y]

    def render(self , screen):
        pygame.draw.rect(screen , RED , (self.pos[0]*CELL_SIZE ,self.pos[1]*CELL_SIZE , CELL_SIZE, CELL_SIZE ))

    def spawn(self , snake_arr):
        self.pos[0] = random.randrange(0 , WINDOW_SIZE[0]//CELL_SIZE)
        self.pos[1] = random.randrange(0 , WINDOW_SIZE[1]//CELL_SIZE)
        if self.pos in snake_arr:
            self.spawn(snake_arr)