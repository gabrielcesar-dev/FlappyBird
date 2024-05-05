import pygame

from .constants import IMAGE_BIRD


class Bird:
    IMGS = IMAGE_BIRD  
    MAX_ROTATION = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5
    JUMP_SPEED = -10.5
    OFFSET_LIMIT = 16
    FALLDOWN_ANGULE = -80
    MAX_ANGULE = -90
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.image_count = 0
        self.image = Bird.IMGS[0]
        
    def jump(self):
        self.speed = Bird.JUMP_SPEED
        self.time = 0 
        self.height = self.y
        
    def move(self):
        self.time += 1
        offset = 1.5 * (self.time**2) + self.speed * self.time
        
        if offset > Bird.OFFSET_LIMIT:
            offset = Bird.OFFSET_LIMIT
        elif offset < 0:
            offset -= 2
            
        self.y += offset
        
        if offset < 0 or self.y < (self.height + 50):
            if self.angle < Bird.MAX_ROTATION:
                self.angle = Bird.MAX_ROTATION
        elif self.angle > Bird.MAX_ANGULE:
            self.angle -= Bird.ROTATION_SPEED
    
    def animation(self, screen):
        self.image = Bird.IMGS[self.image_count // self.ANIMATION_TIME % len(Bird.IMGS)]
        self.image_count = (self.image_count + 1) % (self.ANIMATION_TIME * len(Bird.IMGS))

        if self.angle <= Bird.FALLDOWN_ANGULE:
            self.image = Bird.IMGS[1]
            self.image_count = self.ANIMATION_TIME * 2
            
        routated_image =  pygame.transform.rotate(self.image, self.angle)
        rect = routated_image.get_rect(center=self.image.get_rect(topleft=(self.x,self.y)).center)
        screen.blit(routated_image, rect.topleft)
        
    def get_mask(self):
        return pygame.mask.from_surface(self.image)
        