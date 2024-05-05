import pygame

from .constants import *
from .bird import Bird
from .pipe import Pipe
from .button import Button
from .ground import Ground


class Game:
    def __init__(self):
        self.bird = Bird(100, SCREEN_HEIGHT // 2)
        self.ground = Ground(730) 
        self.pipes = [Pipe(700)]
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.points = 0
        self.game_over = False
        self.flying = False
        self.button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT //2 - 100, IMAGE_RESTART)
        self.cloack = pygame.time.Clock()
        self.status = True
    
    def screen_animation(self):
        self.screen.blit(IMAGE_BACKGROUND, DEFAULT_TOPLEFT)
        self.bird.animation(self.screen)
        
        for pipe in self.pipes:
            pipe.animation(self.screen)
            
        text = FONT_POINTS.render(f"{self.points}", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 2, 20))   
        
        self.ground.animation(self.screen)
        
        pygame.display.update()
        
    def event_detect(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status = False
                pygame.quit()
                quit()
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.game_over == False:
                if self.flying == False:
                    self.flying = True    
                JUMP_FX.play()
                self.bird.jump()
                    
    def reset(self):
        PAUSE_FX.play()
        self.game_over = False
        self.bird = Bird(100, SCREEN_HEIGHT // 2)
        self.points = 0
        self.pipes.clear()
        self.pipes.append(Pipe(700))
        pygame.mixer.music.play(-1, 0.0, 4000)
    
    def action(self):
        if self.flying == True and self.game_over == False:       
                self.bird.move()
                    
                self.ground.move()
                
                new_pipe = False
                remove_pipes = []
                
                for pipe in self.pipes:
                    if pipe.colission(self.bird):
                        self.game_over = True
                        HURT_FX.play()
                        SHOCK_FX.play()

                    if not pipe.bird_pass and self.bird.x > pipe.x:
                        pipe.bird_pass = True
                        new_pipe = True
                        
                    pipe.move()
                    
                    if pipe.x + pipe.image_top.get_width() < 0:
                        remove_pipes.append(pipe)
                
                if new_pipe:
                    self.points += 1
                    POINT_FX.play()
                    
                    self.pipes.append(Pipe(SCREEN_WIDTH + 100))
                
                for pipe in remove_pipes:
                    self.pipes.remove(pipe)
                    
                if self.bird.y + self.bird.image.get_height() > self.ground.y or self.bird.y < 0:
                        self.game_over = True
                        HURT_FX.play()
                        SHOCK_FX.play()
        
    @classmethod
    def run(cls):
        pygame.init()

        pygame.mixer.music.play(-1, 0.0, 5000)
        
        states = Game()

        while states.status:
            states.cloack.tick(30)
            states.event_detect()
            states.action()
                          
            if states.game_over == True and states.flying == True:
                pygame.mixer.music.stop()
                if states.button.animation(states.screen) == True:
                    states.reset()
                                               
            if states.game_over == False:
                states.screen_animation()
    