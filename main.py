import pygame as pg

screen_fill = 50, 50, 50
window_size = 800
screen = pg.display.set_mode([window_size] * 2)

pg.display.set_caption("snake")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    screen.fill(screen_fill)
    pg.display.flip()