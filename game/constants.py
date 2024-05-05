import pygame

import os


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

IMAGE_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'imgs', 'pipe.png')))
IMAGE_GROUND = pygame.transform.scale2x(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'imgs', 'base.png')))
IMAGE_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'imgs', 'bg.png')))
IMAGE_RESTART = pygame.transform.scale2x(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'imgs', 'restart.png')))
IMAGE_BIRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources','imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources','imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources','imgs', 'bird3.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources','imgs', 'bird2.png'))),
]

pygame.mixer.pre_init(44100, -16, 2, 512)

pygame.mixer.init()

pygame.mixer.music.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'sounds', 'music.wav'))

POINT_FX = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'sounds', 'point.wav'))
POINT_FX.set_volume(0.5)
HURT_FX = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'sounds', 'hurt.wav'))
HURT_FX.set_volume(0.5)
JUMP_FX = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'sounds', 'jump.wav'))
JUMP_FX.set_volume(0.5)
PAUSE_FX = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'sounds', 'pause.wav'))
PAUSE_FX.set_volume(0.5)
SHOCK_FX = pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'resources', 'sounds', 'shock.wav'))
SHOCK_FX.set_volume(0.5)

pygame.font.init()

FONT_SIZE = 60
FONT = "Bauhaus 93"
FONT_POINTS = pygame.font.SysFont(FONT, FONT_SIZE)

DEFAULT_TOPLEFT = (0, 0)
WHITE = (255, 255, 255)