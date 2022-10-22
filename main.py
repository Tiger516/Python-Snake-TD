import pygame

background_colour = (50, 50, 50)
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Snake')
pygame.display.set_icon()

screen.fill(background_colour)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False