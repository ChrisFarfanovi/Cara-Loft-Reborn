from tkinter import ttk
import pygame
from pygame.locals import *

# imports
import ttkbootstrap as ttk


# Window
# window = ttk.Window(title="Cara Loft Reborn", themename="darkly")
# window.resizable(True, True)


# Variables
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()  # get a pygame clock object
player = pygame.image.load(
    "Cara_Loft.bmp"
).convert()  # This is in my folder as a bmp file
entity = pygame.image.load(
    "alien1.bmp"
).convert()  # Need to find a way to allow  this to import the file
background = pygame.image.load("Dungeon1.bmp").convert()
screen.blit(background, (0, 0))
objects = []
p = GameObject(player, 10, 3)  # create the player object
for x in range(10):  # create 10 objects</i>
    o = GameObject(entity, x * 40, x)
    objects.append(o)
while True:
    screen.blit(background, p.pos, p.pos)
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(p.image, p.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)
# Chris if you read this, this is the libary i'm trying to play around with
# https://www.pygame.org/docs/
# Output


# Input


# Window Open
