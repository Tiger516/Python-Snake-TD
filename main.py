import imp
import pygame as pg
import os
import time
import random
from random import randint
from time import sleep
from pygame.locals import * 

window_width = 500
window_height = 500
game_display = pg.display.set_mode((window_width, window_height))
window_game_name = "Snake"
running = True
background_colour = (50, 50, 50)
pg.display.set_caption(window_game_name)

game_display.fill(background_colour)
pg.display.flip()

# creating images variebles

apple = pg.image.load(os.path.join('images', 'apple.png'))
apple = pg.transform.scale(apple, (32, 32)) 

snake_head = pg.image.load(os.path.join('images', 'head.png'))
snake_head = pg.transform.scale(snake_head, (32, 32)) 

grid = pg.image.load(os.path.join('images', 'Other-Grid.png'))
grid = pg.transform.scale(grid, (32, 32)) 

snake_body = pg.image.load(os.path.join('images', 'Snake-Body.png'))
snake_body = pg.transform.scale(snake_body, (32, 32)) 

def create_apple(x,y):
    game_display.blit(apple, (x,y))
    
def create_head(x,y):
    game_display.blit(snake_head, (x,y))

create_head(randint(0, window_width - 32), randint(0, window_height - 32))
create_apple(randint(0, window_width - 32), randint(0, window_height - 32))

pg.display.update()

pg.display.set_icon(apple)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
