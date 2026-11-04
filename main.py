import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400,500))

player = pygame.Rect(100,460,40,40)

fps=20
score=0
print(score)
running=True

blocks=[pygame.Rect(random.randint(0,400),0,random.randint(40,300),40),pygame.Rect(random.randint(0,400),0,random.randint(40,300),40)]

timer=0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

#key press logic
    press=pygame.key.get_pressed()
    if press[pygame.K_LEFT]:
        player.x -=5
    if press[pygame.K_RIGHT]:
        player.x +=5


#Keepig player in bound logic
    if player.x>360:
        player.x=360
    if player.x<0:
        player.x=0

#For creating new block every few seconds
    timer+=1
    if timer==3*fps:
        a=pygame.Rect(random.randint(0,400)
        b=random.randint(40,300)
        blocks.append(a,0,b,40))
        blocks.append(pygame.Rect(random.randint(a,400-a),0,random.randint(b,300-b),40))
        timer=0

    for block in blocks:
        block.y+=5
        if player.colliderect(block):
            print("Game over!")
            print("Score ", score)
            running = False;
        if block.y==500:
            score+=1




    screen.fill((20,20,40))
    pygame.draw.rect(screen,(0,255,255),player)
    for block in blocks:
        pygame.draw.rect(screen,(0,200,200),block)
    pygame.display.flip()
    pygame.time.Clock().tick(fps)

pygame.quit()