import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400,500))

font = pygame.font.SysFont(None,36)
font2 = pygame.font.SysFont("PixelifySans-Regular.ttf",20)

player = pygame.Rect(100,460,40,40)

fps=20
score=0
print(score)
running=True

blocks=[pygame.Rect(random.randint(0,400),0,random.randint(40,300),40),pygame.Rect(random.randint(0,400),0,random.randint(40,300),40)]

timer=0
timer2=0

highscore=0
speed=1

game_over=False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if game_over and event.type== pygame.KEYDOWN and event.key == pygame.K_q:
            running=False

        if game_over and event.type== pygame.KEYDOWN and event.key == pygame.K_r:
            block.y=500
            blocks=[]
            timer=0
            score=0
            game_over=False

    if not game_over:
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
        if timer==3*fps/speed:

            b=random.randint(20,300)
            a=random.randint(0,400)
            blocks.append(pygame.Rect(a,0,b,40))
            blocks.append(pygame.Rect(400-a,0,300-b,40))
            timer=0

        for block in blocks:
            block.y+=5*speed
            if player.colliderect(block):
                print("Game over!")
                print("Score ", score)
                game_over=True

                    
            if block.y==500:
                score+=1

        timer2+=1
        if timer2==30*fps:
            speed = speed+0.5
            timer2 =0
            


    screen.fill((20,20,40))
    pygame.draw.rect(screen,(0,255,255),player)

    for block in blocks:
        pygame.draw.rect(screen,(0,200,200),block)


    scoret = str(score/2)
    text= font.render("Score: "+ scoret[:scoret.index('.')],True,(255,255,255))
    hst = font2.render("Highscore: " + str(highscore),True,(255,255,255))
    screen.blit(text,(200-36,0))
    screen.blit(hst,(10,10))

    if game_over:
        if score>highscore:
            highscore=(score/2)
        restart = font2.render("CLICK R TO RESTART",True,(255,255,255))
        restart2 = font2.render("AND Q TO QUIT",True,(255,255,255))
        screen.blit(restart,(130,230))
        screen.blit(restart2,(130,270))


    pygame.display.flip()
    pygame.time.Clock().tick(fps)

pygame.quit()