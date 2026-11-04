import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400,500))

player = pygame.Rect(100,460,40,40)
block = pygame.Rect(random.randint(0,200),0,random.randint(0,400),40)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill((20,20,40))
    pygame.draw.rect(screen,(0,255,255),player)
    pygame.draw.rect(screen,(0,200,200),block)
    pygame.display.flip()
    pygame.time.Clock().tick(20)

pygame.quit()