import pygame

pygame.init()
window = pygame.display.set_mode((500,500),0,32)

background_color=(255,255,255)
window.fill(background_color)
pygame.display.update()

x=0
y=0
width=3
height=3

def rect(x,y):
    pygame.draw.rect(window,(0,0,0),(x,y,width,height))
    pygame.display.update()

def maze1():
    #Boundries
    for i in range(0,501):
        rect(498,i)
    for i in range(0,501):
        rect(i,498)
    for i in range(x,498):
        rect(i,0)
    for i in range(y,498):
        rect(0,i)
    # inner walls     
    for i in range(50,300):
        rect(i,50)
    for i in range(50,200):
        rect(50,i)
    for i in range(250,350):
        rect(50,i)
    for i in range(50,400):
        rect(i,250)
    for i in range(150,250):
        rect(100,i)
    for i in range(100,200):
        rect(i,100)
    for i in range(100,200):
        rect(150,i)
    for i in range(100,250):
        rect(250,i)
    for i in range(0,50):
        rect(300,i)
    for i in range(100,200):
        rect(200,i)
    for i in range(300,500):
        rect(i,100)
    for i in range(50,100):
        rect(350,i)
    for i in range(0,50):
        rect(400,i)
    for i in range(450,500,7):
        rect(i,50)
    for i in range(300,500):
        rect(i,200)
    for i in range(300,450):
        rect(i,150)
    for i in range(100,150):
        rect(450,i)
    for i in range(150,200):
        rect(500,i)
    for i in range(500,500):
        rect(i,150)
    for i in range(250,450):
        rect(100,i)
    for i in range(400,500):
        rect(50,i)
    for i in range(50,200):
        rect(i,500)
    for i in range(0,150):
        rect(i,550)
    for i in range(450,500):
        rect(150,i)
    for i in range(150,300):
        rect(i,400)
    for i in range(300,350,7):
        rect(150,i)
    for i in range(300,400):
        rect(200,i)
    for i in range(200,400):
        rect(i,450)
    for i in range(250,450):
        rect(450,i)
    for i in range(350,450):
        rect(i,400)
    for i in range(250,400):
        rect(i,300)
    for i in range(250,400,7):
        rect(i,350)
maze1()      
pygame.time.delay(10000)

    

    
