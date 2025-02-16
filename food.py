import pygame
import random
import settings

CELL_SIZE = settings.cell_size
WINDOW_SIZE = settings.window_size
RED = (200 , 0 , 0)


class Food:
    def __init__(self, snake_arr):
        self.pos = [0,0]
        self.spawn(snake_arr)

    def render(self , screen):

        pygame.draw.rect(screen , RED , (self.pos[0]*CELL_SIZE ,self.pos[1]*CELL_SIZE , CELL_SIZE, CELL_SIZE ))

    def spawn(self , snake_arr):
        self.pos[0] = random.randrange(0 , WINDOW_SIZE[0]//CELL_SIZE)
        self.pos[1] = random.randrange(0 , WINDOW_SIZE[1]//CELL_SIZE)
        if self.pos in snake_arr:
            self.spawn(snake_arr)