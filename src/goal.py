import pygame
from direction import *

class Robot(pygame.sprite.Sprite):

    def __init__(self, imagepath, width, height, x, y, surface):
        pygame.sprite.Sprite.__init__(self)

        self.imagepath = imagepath
        self.image = pygame.image.load(imagepath)

        self.width = width
        self.height = height

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
