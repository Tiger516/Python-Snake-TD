import pygame

Window_Size = 500
Window_Game_Name = "Snake"
running = True
background_colour = (50, 50, 50)
screen = pygame.display.set_mode([Window_Size] * 2)
pygame.display.set_caption(Window_Game_Name)

screen.fill(background_colour)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False