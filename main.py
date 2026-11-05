import pygame
import random
import asyncio

pygame.init()
screen = pygame.display.set_mode((400,500))
clock= pygame.time.Clock()

async def main():
    font = pygame.font.SysFont(None,36)
    font2 = pygame.font.SysFont("fonts/PixelifySans-Bold.ttf",20)

    player = pygame.Rect(100,460,40,40)
    logo = pygame.Rect(180,150,40,40)

    fps=30
    score=0
    print(score)
    running=True
    started=False

    death = pygame.Surface((400,500))
    death.fill((255,0,0))

    blockimg= pygame.image.load("images/phantom.png").convert_alpha()
    blockimg= pygame.transform.scale(blockimg,(40,40))


    blocks=[pygame.Rect(random.randint(0,400),0,random.randint(40,300),40),pygame.Rect(random.randint(0,400),0,random.randint(40,300),40)]

    user = pygame.image.load("images/user.png").convert_alpha()
    user = pygame.transform.scale(user, (40,40))

    user2 = pygame.image.load("images/user.png").convert_alpha()
    user2 = pygame.transform.scale(user2, (40,40))

    timer=0
    timer2=0

    highscore=0
    speed=1

    death_sound = pygame.mixer.Sound("sounds/death.ogg")
    death_sound.set_volume(0.8)

    start_sound = pygame.mixer.Sound("sounds/start.ogg")
    start_sound.set_volume(0.8)

    bg_sound = pygame.mixer.Sound("sounds/bg.ogg")
    bg_sound.set_volume(0.5)
    bg_sound.play(-1)

    game_over=False

    while running:
        for event in pygame.event.get():

            
            if event.type == pygame.QUIT:
                running=False

            if game_over and event.type== pygame.KEYDOWN and event.key == pygame.K_q:
                speed=1
                block.y=500
                blocks=[]
                timer=0
                timer2=0
                score=0
                bg_sound.play(-1)
                game_over=False
                started=False

            if game_over and event.type== pygame.KEYDOWN and event.key == pygame.K_r:
                speed=1
                block.y=500
                blocks=[]
                timer=0
                timer2=0
                score=0
                bg_sound.play(-1)
                game_over=False

            if not started and event.type== pygame.KEYDOWN and event.key == pygame.K_SPACE:
                started=True
                start_sound.play()


        if not game_over and started:
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
            if timer>=3*fps/speed:

                b=random.choice([40,80,120,160,200,240])
                a=random.randint(0,400)
                blocks.append(pygame.Rect(a,0,b,40))
                blocks.append(pygame.Rect(400-a,0,280-b,40))
                timer=0

            for block in blocks:
                block.y+=5*speed
                if player.colliderect(block):
                    game_over=True
                    death_sound.play()
                    flash=200

            for block in blocks:           
                if block.y>500:
                    score+=1
                    start_sound.play()
                    blocks.remove(block)

            timer2+=1
            if timer2==30*fps:
                speed = speed+0.5
                timer2 =0
                
        screen.fill((20,20,40))

        if not started:
            title= font.render("DODGE BLOCKS", True , (255,255,255))
            tell = font.render("PRESS SPACE",True , (255,255,255))
            tell2 = font.render("TO START",True , (255,255,255))
            screen.blit(title,(100,200))
            screen.blit(tell,(100,250))
            screen.blit(tell2,(130,280))
            pygame.draw.rect(screen,(0,255,255),logo)
            screen.blit(user2 , logo)
            
        if started:
            screen.fill((20,20,40))
            pygame.draw.rect(screen,(0,255,255),player)
            screen.blit(user , player)

            for block in blocks:
                for x in range(block.x , block.right, 40):
                    screen.blit(blockimg,(x,block.y),(0,0,min(40,block.right-x),40))


            scoret = str(score/2)
            text= font.render("Score: "+ scoret[:scoret.index('.')],True,(255,255,255))
            hst = font2.render("Highscore: " + str(highscore//2),True,(255,255,255))
            screen.blit(text,(200-36,0))
            screen.blit(hst,(10,10))

            if game_over:
                bg_sound.stop()
                if flash>0:
                        death.set_alpha(255)
                        screen.blit(death,(0,0))
                        flash-=20
                if score>highscore:
                    highscore=score
                restart = font2.render("CLICK R TO RESTART",True,(255,255,255))
                restart2 = font2.render("AND Q TO RETURN HOME",True,(255,255,255))
                screen.blit(restart,(130,230))
                screen.blit(restart2,(130,270))


        pygame.display.flip()
        clock.tick(fps)
        await asyncio.sleep(0)   


asyncio.run(main())