from lib2to3 import pgen2
import pygame as pg

Window_Size = 500
Window_Game_Name = "Snake"
running = True
background_colour = (50, 50, 50)
screen = pg.display.set_mode([Window_Size] * 2)
pg.display.set_caption(Window_Game_Name)

screen.fill(background_colour)
pg.display.flip()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False