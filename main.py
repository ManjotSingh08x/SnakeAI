import pygame
import random
import time
from snake import Snake
from food import Food

WINDOW_SIZE = (800,600)

MOVE_UP = [0,-1]
MOVE_DOWN = [0,1]
MOVE_LEFT = [-1,0]
MOVE_RIGHT = [1,0]

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.width, self.height = WINDOW_SIZE
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Dumbass \'Python\' Game!!")


        self.font = pygame.font.Font(None, 30)

        self.clock = pygame.time.Clock()

        self.running = True
        self.food = Food(20 , 15)
        self.snake = Snake([[20,20] , [20,21] , [21,21]])
        self.score = 0
        self.game_over = False
        self.init_time = time.time()

    def check_food_collision(self):
        if self.snake.arr[0][0] == self.food.pos[0] and self.snake.arr[0][1] == self.food.pos[1]:
            self.score +=1
            self.food.spawn(self.snake.arr)
            self.snake.arr.append([self.snake.arr[-1][0]+self.snake.dir[0],self.snake.arr[-1][1]+self.snake.dir[1]])
            self.snake.length +=1

    def snake_collision(self):
        future = self.snake.future_head()
        if future in self.snake.arr:
            self.game_over = True
            

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(144)


    def handle_events(self):
        valid = self.snake.dir
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                valid = MOVE_UP
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                valid = MOVE_LEFT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                valid = MOVE_DOWN
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                valid = MOVE_RIGHT
            if valid != [self.snake.arr[1][0] - self.snake.arr[0][0] , self.snake.arr[1][1] - self.snake.arr[0][1] ]:
                self.snake.dir = valid
            
            if event.type==pygame.KEYDOWN and event.key == pygame.K_r and self.game_over:  # Restart game
                self.__init__()

            

    def update(self):
        self.check_food_collision()
        self.snake_collision()
        self.snake.move()

    def render(self):

        elapsed_seconds = int(time.time() - self.init_time)  # Get elapsed seconds
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_seconds))
        if not self.game_over:
            self.screen.fill((0, 0, 0))
            self.snake.draw(self.screen)
            self.food.render(self.screen)




            text_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(text_surface, (20, 20))

            atime = self.font.render(f"Time: {formatted_time}", True, (255, 255, 255))
            self.screen.blit(atime, (WINDOW_SIZE[0]-atime.get_width()-20, 20))
        
        else:
            self.screen.fill((12,12,12))
            final_score = pygame.transform.scale2x(self.font.render(f'The final Score: {self.score}' , True , (255 , 0 , 0)))
            self.screen.blit(final_score, (400 - final_score.get_width()//2, 300 - final_score.get_height()//2))
            retry_text = self.font.render("Press R to Restart", True, (200, 200, 200))
            self.screen.blit(retry_text, (400 - retry_text.get_width()//2, 400))
            time_text = self.font.render(f"Your time being here: {formatted_time}", True, (200, 200, 200))
            self.screen.blit(time_text , (400 - final_score.get_width()//2, 100 - final_score.get_height()//2))


        pygame.display.flip()

    def quit(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
    game.quit()
 


