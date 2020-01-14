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

        self.dx = 1
        self.dy = 0

        self.action_list = []

        self.destx = 0
        self.desty = 0
        self.is_moving = False

    def move(self, collidables):
        sprite_list = collidables.sprites()
        self.destx = self.rect.x + self.width * self.dx
        self.desty = self.rect.y + self.height * self.dy
        dest_rect = pygame.Rect(self.destx, self.desty, self.width, self.height)
        for collidable in sprite_list:
            if (not dest_rect.colliderect(collidable)):
                self.is_moving = True

    def set_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def turn(self, direction):
        if(direction == Direction.RIGHT):
            temp = - self.dy
            self.dy = self.dx
            self.dx = temp
        elif(direction == Direction.LEFT):
            temp = - self.dx
            self.dx = self.dy
            self.dy = temp

    def baby_step(self):
        if(not self.is_moving):
            return
        self.rect.x += 2*self.dx
        self.rect.y += 2*self.dy
        if(self.destx == self.rect.x and self.desty == self.rect.y):
            self.is_moving = False

    def set_action_list(self, action_list):
        self.action_list = action_list

    def execute_action(self, collidables):
        if len(self.action_list) != 0:
            self.action_list.pop(0).execute(self, collidables)

    def add_action(self, action):
        self.action_list.append(action)
