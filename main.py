import pygame as pg
import os

Window_Size = 500
Window_Game_Name = "Snake"
running = True
background_colour = (50, 50, 50)
screen = pg.display.set_mode([Window_Size] * 2)
pg.display.set_caption(Window_Game_Name)

screen.fill(background_colour)
pg.display.flip()

Apple = pg.image.load(os.path.join('images', 'apple.png'))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False