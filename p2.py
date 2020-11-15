import pygame,sys
import time
import random
pygame.init()
display_width=1000
display_height=800
gray=(128,128,128)
black=(0,0,0)
red=(255,0,0)
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("car game")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.png')
backgroundpic=pygame.image.load('download12.jpg')
yellow_strip=pygame.image.load('yellostrip.png')
car_width=93
intro_background=pygame.image.load("instruction.jpg")
instruct=pygame.image.load("instruction.jpg")
green_bright_green=(0, 255, 0)
red_bright_red=(255,0,0)
blue_bright_blue=(0,255,255)
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()
def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=(display_width//2,display_height//2)
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(1)
    game_loop()

def pause():
    intro=True
    while intro:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruct, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        textsurf, textrect = text_objects("PAUSED", largetext)
        textrect.center = (500, 100)
        gamedisplays.blit(textsurf, textrect)
        button("RESTART", 150, 550, 100, 50, green_bright_green, "play")
        button("CONTINUE", 350, 550, 150, 50, red, "continue")
        button("MENU", 550, 550, 100, 50, blue_bright_blue, "menu")
        pygame.display.update()
        clock.tick(50)



def crush():
    message_display("YOU ARE CRASHED")
def car(x,y):
    gamedisplays.blit(carimg,(x,y))
def introduction():
    intro= True
    while intro:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruct, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        textsurf, textrect = text_objects("INSTRUCTIONS", largetext)
        textrect.center = (500, 100)
        gamedisplays.blit(textsurf, textrect)
        smalltext = pygame.font.Font("freesansbold.ttf", 35)
        textsurf, textrect = text_objects("UP LEFT RIGHT DOWN", smalltext)
        textrect.center = (200, 500)
        gamedisplays.blit(textsurf, textrect)
        textsurf, textrect = text_objects("SPEED INCREASES WHILE INCREASING LEVEL", smalltext)
        textrect.center = (420, 550)
        gamedisplays.blit(textsurf, textrect)
        textsurf, textrect = text_objects("JASHWANTH", smalltext)
        textrect.center = (200, 600)
        gamedisplays.blit(textsurf, textrect)
        button("BACK", 750,720, 100, 50, blue_bright_blue, "menu")
        pygame.display.update()
        clock.tick(50)

def button(msg,x,y,w,h,ac,action=None):
    mouse =pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if(x+w>mouse[0]>x and y+h>mouse[1]>y):
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if(click[0]==1 and action!=None):
            if(action=="play"):
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                pause()
    else:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)
def countdown_background():
    font=pygame.font.SysFont(None,40)
    x=(display_width*0.45)
    y=(display_height*0.7)
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(yellow_strip, (500, 0))
    gamedisplays.blit(yellow_strip, (500, 150))
    gamedisplays.blit(yellow_strip, (500, 350))
    gamedisplays.blit(yellow_strip, (500, 550))
    gamedisplays.blit(yellow_strip, (500, 750))
    gamedisplays.blit(backgroundpic, (900, 0))
    gamedisplays.blit(carimg,(x,y))
def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()


def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background, (0,0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        textsurf, textrect = text_objects("Car Game", largetext)
        textrect.center=(500,100)
        gamedisplays.blit(textsurf, textrect)
        button("START",150,520,100,50,green_bright_green,"play")
        button("QUIT", 350, 520, 100, 50, red, "quit")
        button("INSTRUCTIONS", 550, 520, 200, 50, blue_bright_blue, "intro")
        pygame.display.update()
        clock.tick(50)

def obstacle(obs_startx,obs_starty,obs):

    if(obs == 0):
        obs_pic=pygame.image.load("car2.png")
    elif(obs == 1):
        obs_pic=pygame.image.load("car2.png")
    elif (obs == 2):
        obs_pic = pygame.image.load("car3.png")
    elif (obs == 3):
        obs_pic = pygame.image.load("car4.png")
    elif (obs == 4):
        obs_pic = pygame.image.load("car5.png")
    elif (obs == 5):
        obs_pic = pygame.image.load("car6.png")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

def score_system(passed,score):
    font=pygame.font.SysFont(None,40)
    text=font.render("passed"+"="+str(passed),True,red)
    score=font.render("score"+"="+str(score),True,red)
    gamedisplays.blit(text,(110,70))
    gamedisplays.blit(score,(110,30))

def game_loop(score=0,passed=0,level=0):
    bumped=False
    x=(display_width*0.45)
    y=(display_height*0.7)
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-800
    obs_width=97
    obs_height=213
    y2=7

    while not bumped:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_LEFT):
                    x_change=-5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if(event.key==pygame.K_a):
                    obstacle_speed+=2
                if (event.key == pygame.K_b):
                    obstacle_speed -= 2
            if(event.type==pygame.KEYUP):
                if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                    x_change=-0

        x+=x_change
        gamedisplays.fill(gray)
        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic, (900, rel_y - backgroundpic.get_rect().width))
        if(rel_y<900):
            gamedisplays.blit(backgroundpic, (0, rel_y+0))
            gamedisplays.blit(yellow_strip, (500, rel_y+(-10)))
            gamedisplays.blit(yellow_strip, (500, rel_y+150))
            gamedisplays.blit(yellow_strip, (500, rel_y+350))
            gamedisplays.blit(yellow_strip, (500, rel_y+550))
            gamedisplays.blit(yellow_strip, (500, rel_y+750))
            gamedisplays.blit(backgroundpic, (900, rel_y+0))
        y2+=obstacle_speed
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        score_system(passed,score)
        car(x,y)

        if x>990-car_width or x<36:
            crush()
        if x>display_width-(car_width+36) or x<36:
            crush()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(180,(display_width-180))
            obs=random.randrange(0,5)
            passed = passed + 1
            score=passed*10
            if int(passed%10)==0:
                level=level+1
                obstacle_speed+=2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("LEVEL"+" "+str(level)+"!", largetext)
                textrect.center = (display_width // 2, display_height // 2)
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(1)
        if(y<obs_starty+obs_height):
            if x>obs_startx and x<obs_startx+obs_width or x+car_width>obs_startx and x+car_width<obs_startx+obs_width:
                crush()
        button("PAUSE",800,0,100,50,blue_bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)
intro_loop()
game_loop()
pygame.quit()
quit()