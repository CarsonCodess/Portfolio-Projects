import pygame
import time
import random
import sys
pygame.font.init()
pygame.mixer.init()

#Changed:
#Starting Screen
#Player velocity slowly increase
#Sound
#Made screen fullscreen (Make it resizable when you can)
#Made pause menu (Add a quit button and a main menu button)

#To Do:
#Fix fade screen, make sure to give Pix credit
#Sprites (Images are made but now add it to game)
#Make it lose sometimes randomly (more random gameplay)
#Better Title Screen
#Maybe customizable sprites

#Screen -----------------------------------------------------------
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
WIDTH, HEIGHT = WIN.get_width(), WIN.get_height()
pygame.display.set_caption("Pong")

BG = pygame.transform.scale(pygame.image.load("Pong\\bg.jpg"), (WIDTH, HEIGHT))
# -----------------------------------------------------------------
# -----------------------------------------------------------------
#Game Variables ---------------------------------------------------
PLAYER_SCORE = 0
ENEMY_SCORE = 0

PLAYER_WIDTH, PLAYER_HEIGHT = 10, 75
PLAYER_VEL = 7

ENEMY_WIDTH, ENEMY_HEIGHT = 10, 75
ENEMY_VEL = 7.5

STAR_WIDTH = 15
STAR_HEIGHT = 15
STAR_RADIUS = 15
STAR_VEL = 6
# -------------------------------------------------------------------
# -------------------------------------------------------------------
#Font ---------------------------------------------------------------
FONT = pygame.font.SysFont("comicsans", 30)
STARTFONT = pygame.font.SysFont("arialblack", 40)
RESUMEFONT = pygame.font.SysFont("arialblack", 30)
# -------------------------------------------------------------------
# -------------------------------------------------------------------
#Draws stuff to the screen ------------------------------------------
def draw(player, elapsed_time, star, enemy, PLAYER_SCORE, ENEMY_SCORE):
    WIN.blit(BG, (0,0))

    #time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    #WIN.blit(time_text, (WIDTH/2, 10))

    player_score_text = FONT.render(f"Player: {PLAYER_SCORE}", 1, "white")
    WIN.blit(player_score_text, (WIDTH/8.4, 10))

    enemy_score_text = FONT.render(f"Enemy: {ENEMY_SCORE}", 1, "white")
    WIN.blit(enemy_score_text,(WIDTH/1.33, 10))

    pygame.draw.rect(WIN, "white", player)
    pygame.draw.rect(WIN, "red", star)
    pygame.draw.rect(WIN, "white", enemy)

    pygame.display.update()
# -------------------------------------------------------------------

def main(PLAYER_SCORE, ENEMY_SCORE, faded):
    run = True

    hitx = False
    hity = False

    hitsound = (pygame.mixer.Sound("Pong\\ballhitpaddle.wav"))
    scoresound = (pygame.mixer.Sound("Pong\\ballscore.wav"))
    hitsound.set_volume(0.2)
    scoresound.set_volume(0.2)

    player = pygame.Rect(WIDTH/12, HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)

    enemy = pygame.Rect(WIDTH/1.1, HEIGHT/2, ENEMY_WIDTH, ENEMY_HEIGHT)

    star = pygame.Rect(WIDTH/2, HEIGHT/2, STAR_WIDTH, STAR_HEIGHT)

    clock = pygame.time.Clock()
    elapsed_time=0

    speedmult = 0

    start = 1

    start_time = time.time()

    #Flips who the ball is fed to at first ------------------------------
    if((ENEMY_SCORE + PLAYER_SCORE) % 2 != 0):
        hitx=True
    # -------------------------------------------------------------------

    while run:
        
        #Starts game timer and fixes the -1 issue
        clock.tick(60)
        elapsed_time=time.time()-start_time-1
        if(elapsed_time<0):
            elapsed_time = 0

        #Checks if they have clicked the quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            #Pause Screen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True
                    while paused == True:
                        resume_text = RESUMEFONT.render(f"RESUME", 1, "white")

                        mouse = pygame.mouse.get_pos() 

                        bgmusic = pygame.mixer.Sound("Pong\\bgmusicbyPixonyoutube.wav")
                        bgmusic.play(-1)

                        while paused == True: 
                            
                            for event in pygame.event.get(): 
                                
                                if event.type == pygame.QUIT: 
                                    pygame.quit() 
                                    
                                #checks if a mouse is clicked 
                                if event.type == pygame.MOUSEBUTTONDOWN: 
                                    
                                    #if the mouse is clicked on the 
                                    # button the game starts
                                    if WIDTH/2.3 <= mouse[0] <= WIDTH/2.3+165 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+60: 
                                        bgmusic.fadeout(3000)
                                        intensebgmusic = pygame.mixer.Sound("Pong\\intensemusicbyPixonyoutube.wav")
                                        intensebgmusic.play(-1)
                                        paused=False

                            #Gets mouse position
                            mouse = pygame.mouse.get_pos() 

                            #Checks if the mouse is in the proper spot
                            if WIDTH/2.3 <= mouse[0] <= WIDTH/2.3+165 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+60: 
                                pygame.draw.rect(WIN,"red",[WIDTH/2.3,HEIGHT/2,165,60]) 
                            
                            else: 
                                pygame.draw.rect(WIN,"black",[WIDTH/2.3,HEIGHT/2,165,60]) 
                            
                            #Draws text on screen
                            WIN.blit(resume_text, ((WIDTH/2.3)+10,HEIGHT/2)) 

                            pygame.display.update()

        #Checks elapsed time to add to speedmult
        if (round(elapsed_time, 1)%10 == 0):
            speedmult += 0.1

        #Movement for player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.y -= (PLAYER_VEL + (speedmult/2))
        if keys[pygame.K_DOWN]:
            player.y += (PLAYER_VEL + (speedmult/2))
        if player.y <= 0:
            player.y = 0
        if player.y >= HEIGHT-PLAYER_HEIGHT:
            player.y = HEIGHT-PLAYER_HEIGHT

        #Movement for enemy
        if(enemy.y <= 0):
            enemy.y = 0
        if(enemy.y >= HEIGHT-ENEMY_HEIGHT):
            enemy.y = HEIGHT-ENEMY_HEIGHT
        if(star.y > enemy.y):
            enemy.y += (ENEMY_VEL + (speedmult/4))
        if(star.y < enemy.y):
            enemy.y -= (ENEMY_VEL + (speedmult/4))

        #Checks if star hits enemy
        if (star.x + star.height >= enemy.x and star.colliderect(enemy)):
            hitx = False

            hitsound.play()

            #Changes which way the pong goes randomly
            randomint = random.randint(0, 10)
            if randomint <= 3:
                hity = not hity

        #Changes which way the pong moves
        if(hity==False):
            star.y += STAR_VEL + speedmult
        if(hity==True):
            star.y -= STAR_VEL + speedmult
        if(hitx==False):
            star.x -= STAR_VEL + speedmult
        if(hitx==True):
            star.x += STAR_VEL + speedmult

        #Checks if star hits player
        if (star.x + star.height >= player.x and star.colliderect(player)):
            hitx=True
            
            hitsound.play()

            #Changes which way the pong goes randomly
            randomint = random.randint(0, 10)
            if randomint <= 3:
                hity = not hity
        
        #Checks if star hits ceiling or floor
        if (star.y + star.height >= HEIGHT):
            hity = True
        if (star.y <= 0):
            hity = False

        #Checks if star hits wall and adds score
        if (star.x + star.width <= 0):
            ENEMY_SCORE += 1

            scoresound.play()

            main(PLAYER_SCORE, ENEMY_SCORE, True)
        if (star.x + star.width >= WIDTH):
            PLAYER_SCORE += 1

            scoresound.play()

            main(PLAYER_SCORE, ENEMY_SCORE, True)
        
        #Calls draw function
        draw(player, elapsed_time, star, enemy, PLAYER_SCORE, ENEMY_SCORE)


        #Delays the start
        if(start == 1):
            pygame.time.delay(1000)
            start+=1
    
    pygame.quit()




#Start Menu
def startmenu():
    WIN.blit(BG, (0,0))
    start_text = STARTFONT.render(f"START", 1, "white")

    fade_counter = 0

    mouse = pygame.mouse.get_pos() 

    bgmusic = pygame.mixer.Sound("Pong\\bgmusicbyPixonyoutube.wav")
    bgmusic.play(-1)

    while True: 
        
        for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                
                #if the mouse is clicked on the 
                # button the game starts
                if WIDTH/2.3 <= mouse[0] <= WIDTH/2.3+165 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+60: 
                    bgmusic.fadeout(3000)
                    #Makes fade screen
                    while(fade_counter < WIN.get_width()):
                        fade_counter += 4
                        print(fade_counter)
                        pygame.draw.rect(WIN, "black", (0, 0, fade_counter, WIN.get_height()))
                        pygame.display.update()
                        pygame.time.delay(1)
                    intensebgmusic = pygame.mixer.Sound("Pong\\intensemusicbyPixonyoutube.wav")
                    intensebgmusic.play(-1)
                    main(PLAYER_SCORE, ENEMY_SCORE, False)

        #Gets mouse position
        mouse = pygame.mouse.get_pos() 

        #Checks if the mouse is in the proper spot
        if WIDTH/2.3 <= mouse[0] <= WIDTH/2.3+165 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+60: 
            pygame.draw.rect(WIN,"red",[WIDTH/2.3,HEIGHT/2,165,60]) 
          
        else: 
            pygame.draw.rect(WIN,"black",[WIDTH/2.3,HEIGHT/2,165,60]) 
        
        #Draws text on screen
        WIN.blit(start_text, ((WIDTH/2.3)+10,HEIGHT/2)) 

        pygame.display.update()

if __name__ == "__main__":
    startmenu()