import pygame
import sys
import os
from robot import *
from pygame.locals import *
from action import *

def load_sprites():
    robot = Robot("robot.png", 50, 50, 200, 200, screen)
    sprites.add(robot)
    objects['robot'] = robot

def main():
    # objects.get('robot').set_action_list([Action_move, Action_turn_left, Action_move, Action_turn_right, Action_move])

    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_e:
                    objects.get('robot').execute_action(sprites)
                if event.key == K_m:
                    objects.get('robot').add_action(Action_move)
                if event.key == K_a:
                    objects.get('robot').add_action(Action_turn_left)
                if event.key == K_d:
                    objects.get('robot').add_action(Action_turn_right)

        objects.get('robot').baby_step()
        pygame.time.Clock().tick(fps)
        screen.blit(background, (0,0))
        sprites.draw(screen)
        pygame.display.flip()

pygame.init()

fps = 30
fps_clock = pygame.time.Clock()

screen = pygame.display.set_mode((900, 675))
background =  pygame.Surface(screen.get_size())
background.fill((0,255,0))
background = background.convert()

sprites = pygame.sprite.Group()
objects = {}
load_sprites()

main()
