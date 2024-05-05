import pygame

import random

from .constants import IMAGE_PIPE


class Pipe:
    DISTANCE = 250
    SPEED = 5
    HEIGHT_LOWER_LIMIT = 50
    HEIGHT_UPPER_LIMIT = 450
    
    def __init__(self, x):
        self.x = x
        self.heigh = 0
        self.top = 0
        self.down = 0
        self.image_top = pygame.transform.flip(IMAGE_PIPE, False, True)
        self.image_down = IMAGE_PIPE
        self.bird_pass = False
        self.define_heigh()
        
    def define_heigh(self):
        self.heigh = random.randrange(Pipe.HEIGHT_LOWER_LIMIT, Pipe.HEIGHT_UPPER_LIMIT)
        self.top = self.heigh - self.image_top.get_height()
        self.down = self.heigh + Pipe.DISTANCE
        
    def move(self):        
        self.x -= self.SPEED
    
    def animation(self, screen):
        screen.blit(self.image_top, (self.x, self.top))
        screen.blit(self.image_down, (self.x, self.down))
        
    def colission(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.image_top)
        down_mask = pygame.mask.from_surface(self.image_down)
        
        offset_top = (self.x - bird.x, self.top - round(bird.y))
        offset_down = (self.x - bird.x, self.down - round(bird.y))
        
        overlap_top = bird_mask.overlap(top_mask, offset_top)
        overlap_down = bird_mask.overlap(down_mask, offset_down)
        
        if overlap_down or overlap_top:
            return True
        else:
            return False