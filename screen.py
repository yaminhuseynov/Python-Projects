import pygame, random

#initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Irgendwas")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()


#The main game loop 
working = True
while working:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
        
            
    #Fill the display
    display_surface.fill((0, 255, 0))


    #Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()