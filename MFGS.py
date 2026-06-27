import sys
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (50, 150, 255)  

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game Screen")

clock = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)  

    pygame.display.flip()

  
    clock.tick(60)

pygame.quit()
sys.exit()
