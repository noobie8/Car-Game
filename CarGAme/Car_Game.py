# Importing Llibraries
from cgitb import grey
import pygame
import time
import random

#Setup Window For the Game

pygame.init()
grey=(60,60,60)
black=(255,0,0)
display = pygame.display.set_mode((830,600)) #Dimension of Screen
pygame.display.set_caption("Python Race With Noobie")

#Setting Car 
car_img=pygame.image.load("car1.png")
background_left=pygame.image.load("left.png")
background_right = pygame.image.load("left.png")
car_width = 23

def police_car(police_startx,police_starty,police):
    if police==0:
        police_come = pygame.image.load("car2.png")
    if police==1:
        police_come= pygame.image.load("car3.png")
    if police==2:
        police_come=pygame.image.load("car1.png")
    display.blit(police_come,(police_startx,police_starty))

def background():
    display.blit(background_left,(0,0))
    display.blit(background_right,(700,0))


#Fn for restart while crashing
def crash():
    message_display("Game Over :)")

def message_display(text):
    large_text=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_object(text,large_text)
    textrect.center=((400),(300))
    display.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    loop()

def text_object(text,font):
    text_surface=font.render(text,True,black)
    return text_surface,text_surface.get_rect()


#seting Car position 
def car(x,y):
    display.blit(car_img,(x,y))

def loop():
    x=400
    y=540
    x_change=0
    y_change=0

    police_car_speed = 9
    police=0
    police_startx=random.randrange(130,(700-car_width))
    police_starty=-600
    police_width=23
    police_height=47


#motion of car

bumped=False

while not bumped:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
#defining arrow keys
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-1
            if event.key==pygame.K_RIGHT:
                x_change=1
        if event.type==pygame.KEYUP:
            x_change=0
        
    x+=x_change


#apply restirictions to the cars
display.fill("gray")
background()
police_starty-=(police_car_speed/1.2)
police_car(police_startx,police_starty,police)
police_starty+=police_car_speed
car(x,y)

if x<130 or x>700-car_width:
    crash()


# For random Police

if police_starty>600:
    police_starty=0-police_height
    police_startx=random.randrange(130,(1000,300)) #
    police=random.randrange(0,2)

if y<police_starty+police_height:
    if x> police_startx and x < police_startx + police_width or x + car_width >police_startx and x +car_width < police_startx + police_width :
        crash()



#For Exit

pygame.display.update()
loop()
pygame.quit()
quit()