
import pygame,sys
from pygame.locals import *
import time
import random
pygame.init()


width=800
height=600
screen=pygame.display.set_mode((width, height))

screen.fill((255,255,255))
pygame.display.set_caption("my_game")
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)

backgr=pygame.image.load('day.png')
backgr=pygame.transform.scale(backgr,(width,height))
screen.blit(backgr,(0,0))
spaceship=pygame.image.load('spaceship.png')
spaceship=pygame.transform.scale(spaceship,(50,50))
screen.blit(spaceship,(325,550))
crash_sound=pygame.mixer.Sound("smb_gameover.wav")
pygame.mixer.music.load("MushroomKingdom.mid")
def change(coscore):
       coscore-=10
       return coscore
def score(count):
    font=pygame.font.SysFont(None,25)
    txt=font.render("score :"+str(coscore+10),True,(0,0,0))
    screen.blit(txt,(0,0))
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255,255,255))
        largetxt=pygame.font.Font("freesansbold.ttf",100)
        txtsurf,txtrect=text_object("my game",largetxt)
        txtrect.center=(width/2,height/2)
        screen.blit(txtsurf,txtrect)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 150+100>mouse[0]>150 and 450+50>mouse[1]>450:
            pygame.draw.rect(screen,(0,150,0),(150,450,100,50))
            if click[0]==1 :
                gameloop(90)
        else:
            pygame.draw.rect(screen,green,(150,450,100,50))
        stxt=pygame.font.Font("freesansbold.ttf",20)
        txtsurf,txtrect=text_object("play",stxt)
        txtrect.center=((150+(100/2)),(450+(50/2)))
        screen.blit(txtsurf,txtrect)
        
        if 550+100>mouse[0]>550 and 450+50>mouse[1]>450:
            pygame.draw.rect(screen,(200,0,0),(550,450,100,50))
            if click[0]==1:
                pygame.quit()
                sys.exit()
            
        else:
            pygame.draw.rect(screen,red,(550,450,100,50))
        textsurf,textrect=text_object("quit",stxt)
        textrect.center=((550+(100/2)),(450+(50/2)))
        screen.blit(textsurf,textrect)

        pygame.display.update()       
            

def things(thingx,thingy,thingw,thingh,col):
    pygame.draw.rect(screen,col,[thingx,thingy,thingw,thingh])
def text_object(txt,font):
    txtsurface=font.render(txt,True,(0,0,0))
    return txtsurface,txtsurface.get_rect()
def message_show(txt):
    largetxt=pygame.font.Font("freesansbold.ttf",100)
    txtsurf,txtrect=text_object(txt,largetxt)
    txtrect.center=(width/2,height/2)
    screen.blit(txtsurf,txtrect)
    pygame.display.update()
    time.sleep(2)

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_show("game over")
    game_intro()

def gameloop(cs):
    pygame.mixer.music.play(-1)
    global x,y,x1,y1,up,coscore,coscore_change
    coscore_change=0
    coscore=cs
    x=(width*0.45)
    y=(height*0.8)
    up=0
    right_left_move=0
    thing_startx=random.randrange(0,width)
    thing_starty=-600
    thingspeed=5
    thing_width=100
    thing_height=100
    counter=0
    clock=pygame.time.Clock()
    

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    right_left_move=-5
                elif event.key==pygame.K_RIGHT:
                    right_left_move=+5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    right_left_move=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    up=1
                    x1=x+25
                    y1=y
                 
        if up==1:
            pygame.draw.circle(screen,red,(int(x1),int(y1)),10)
            y1-=5
            if y1-10>=thing_starty and y1-10<=thing_starty+thing_width:
                if x1>=thing_startx and x1<=thing_startx+thing_height:
                    thing_startx-=200
                    
        pygame.display.update()
        x+=right_left_move
        screen.fill((255,255,255))
        screen.blit(backgr,(0,0))
        screen.blit(spaceship,(x,y))
        things(thing_startx,thing_starty,thing_width,thing_height,blue)
        thing_starty+=thingspeed
    
        score(counter)
        if x>width-50 or x<0:
            coscore=change(coscore)
            if coscore==-10:
                crash()
            else:
                gameloop(coscore)
    
        if thing_starty>height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,width)
            counter+=1
            if counter%5==0:
                thingspeed+=2
        if y<thing_starty+thing_height:
            if x>thing_startx and x<thing_startx+thing_width or x+50>thing_startx and x+thing_width<thing_startx+thing_width:
                coscore=change(coscore)
                if coscore==-10:
                    crash()
                else:
                    gameloop(coscore)
               

        pygame.draw.rect(screen,(50,50,0),(0,50,100,50),10)
        pygame.draw.rect(screen,(255,242,0),(5,50,coscore,50))
            
                    
                
        pygame.display.update()
        clock.tick(60)
game_intro()
gameloop()
pygame.quit()
sys.exit()
