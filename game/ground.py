from .constants import IMAGE_GROUND


class Ground:
    SPEED = 5
    WIDTH = IMAGE_GROUND.get_width()
    
    def __init__(self, y):
        self.y = y
        self.x_first_ground = 0
        self.x_second_ground = Ground.WIDTH
    
    def move(self):
        if self.x_first_ground + Ground.WIDTH < 0:
            self.x_first_ground = self.x_second_ground + Ground.WIDTH
        elif self.x_second_ground + Ground.WIDTH < 0:
            self.x_second_ground = self.x_first_ground + Ground.WIDTH
            
        self.x_first_ground -= Ground.SPEED
        self.x_second_ground -= Ground.SPEED
    
    def animation(self, screen):
        screen.blit(IMAGE_GROUND, (self.x_first_ground, self.y))
        screen.blit(IMAGE_GROUND, (self.x_second_ground, self.y))