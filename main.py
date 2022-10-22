import pygame

# choosing the background color
background_colour = (50, 50, 50)

# making the screen var
screen = pygame.display.set_mode((500, 500))

# naming the window
pygame.display.set_caption('Snake')

# filling the background up with the colour you put in the var
screen.fill(background_colour)
# flips the display
pygame.display.flip()

# sets running as true
running = True
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False