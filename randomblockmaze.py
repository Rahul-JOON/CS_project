import pygame as p
import random as r
import math as m
import os

p.init()

win = p.display.set_mode((1100, 700))
p.display.set_caption("TankBusters")

run = True

def newcolor():
    colorcodes = r.randint(0, 255)
    return colorcodes

class player():
    def __init__(self, x , y, radius):
        self.x = x 
        self.y = y
        self.radius = radius
        self.vel = 7
        self.deg = 0
    def animate(self, win):
        win.blit(p.image.load(os.path.join('Resources', f'tr{self.deg}.png')).convert() , (self.x, self.y) )
    
class gun():
    def __init__(self, x, y, radius, deg):
        self.x = x 
        self.y = y 
        self.radius = radius 
        self.deg = deg
        self.vel = 10
    def animate(self, win):
        p.draw.circle(win, (0 ,255, 255), (self.x, self.y), self.radius)

class obstructions():
    def __init__(self):
        self.x = r.randint(0, 1436)
        self.y = r.randint(0, 700)
        self.width = r.randint(30, 64)
        self.height = r.randint(30, 128)
        self.dim = (self.x, self.y, self.width, self.height)

    def animate(self, win):
        p.draw.rect(win, (newcolor(), newcolor(), newcolor()), self.dim)


tank = player(200, 200, 40)
enemy = player(100, 100, 40)
enemyt = True
bullets = []
clock = p.time.Clock()
wall = True
walls = []

while run:
    p.time.delay(35)
    clock.tick(120)
    
    for b in bullets:
        if b.y < 700 and b.y > 0 and b.x > 0 and b.x < 1000:
            b.y -= round(m.cos(((m.pi)/180) * b.deg ) * b.vel)
            b.x += round(m.sin(((m.pi)/180) * b.deg) * b.vel)
        else :
            bullets.pop(bullets.index(b))
        if round(((enemy.y - b.y)**2 + (enemy.x - b.x)**2)**(1/2)) <= enemy.radius:
            enemyt = False


    if wall:
        for i in range(50):
            walls.append(obstructions())
            wall = False
             

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    keys = p.key.get_pressed()

    if keys[p.K_UP]:
        tank.y -= round(m.cos(((m.pi)/180) * tank.deg ) * tank.vel)
        tank.x += round(m.sin(((m.pi)/180) * tank.deg) * tank.vel)
    if keys[p.K_DOWN]:
        tank.y += round(m.cos(((m.pi)/180) * tank.deg) * tank.vel)
        tank.x -= round(m.sin(((m.pi)/180) * tank.deg) * tank.vel)

    if keys[p.K_RIGHT]:
        tank.deg += 15
    if keys[p.K_LEFT]:
        tank.deg -= 15

    if keys[p.K_SPACE]:
        bullets.append(gun(tank.x + 32, tank.y + 32, 5, tank.deg))
    
    if tank.deg == 360:
        tank.deg = 0
    elif tank.deg < 0:
        tank.deg = 345

    win.fill((255, 255, 255))
    for wal in walls:
        wal.animate(win)
    for bullet in bullets:
        bullet.animate(win)
    tank.animate(win)
    if enemyt :
        p.draw.circle(win, (0, 155, 0), (enemy.x, enemy.y), enemy.radius)
    
    p.display.flip()

p.quit()