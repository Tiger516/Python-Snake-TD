import imp
import pygame as pg
import os
import random
from random import randint

window_width = 500
window_height = 500
game_display = pg.display.set_mode((window_width, window_height))
window_game_name = "Snake"
running = True
background_colour = (50, 50, 50)
pg.display.set_caption(window_game_name)

game_display.fill(background_colour)
pg.display.flip()

apple = pg.image.load(os.path.join('images', 'apple.png'))
apple = pg.transform.scale(apple, (32, 32)) 

def create_apple(x,y):
    game_display.blit(apple, (x,y))


create_apple(randint(0, window_width - 32), randint(0, window_height - 32))
    
pg.display.update()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
