import pygame

#initailazation
pygame.init()

#display here, >>((800, 600))<< you can tell your height and length in pixels
screen = pygame.display.set_mode((800, 600))

#Text and icon
pygame.display.set_caption("name of your window")
icon = pygame.image.load('joystick.png')
pygame.display.set_icon(icon)
