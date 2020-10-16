import pygame as p
import random as r
import math as m
import os

p.init()

win = p.display.set_mode((1100, 700))
p.display.set_caption("TankBusters")

run = True

class player():
    def __init__(self, x , y, width, height):
        self.x = x 
        self.y = y
        self.height = height
        self.width = width
        self.vel = 7
        self.deg = 0
        self.dim = p.Rect(self.x, self.y, self.width, self.height)
        
    def movementcheck(self, tank, walls):    
        self.tank = tank
        self.walls = walls
        for wall in self.walls:
            if self.tank.dim.colliderect(wall.dim):
                return 'n' 

    def animate(self, win):
        win.blit(p.image.load(os.path.join('Resources/Tanks Animations', f'tr{self.deg}.png')).convert() , (self.x, self.y) )
    
class gun():
    def __init__(self, x, y, radius, deg):
        self.x = x 
        self.y = y 
        self.radius = radius 
        self.deg = deg
        self.vel = 10

    def bounce(self, bullet, walls):
        self.bullet = bullet 
        self.walls = walls
        for wall in walls:
            p1 = (wall.dim[0], wall.dim[1])
            p2 = (wall.dim[0] + wall.dim[2], wall.dim[1])
            p3 = (wall.dim[0] + wall.dim[2], wall.dim[1] + wall.dim[3])
            p4 = (wall.dim[0], wall.dim[1] + wall.dim[3])
            lines = [(p1, p2, wall.dim[2]), (p3, p4, wall.dim[2]), (p1, p4, wall.dim[3]), (p2, p3, wall.dim[3])]
            for line in lines:
                AB = [line[1][0] - line[0][0], line[1][1] - line[0][1]]
                BE = [self.bullet.x - line[1][0], self.bullet.y - line[1][1]]
                AE = [self.bullet.x - line[0][0], self.bullet.y - line[0][1]]
                AB_BE = AB[0] * BE[0] + AB[1] * BE[1] 
                AB_AE = AB[0] * AE[0] + AB[1] * AE[1]
                distance = 0
                if AB_BE > 0:
                    y = self.bullet.y - line[1][1]
                    x = self.bullet.x - line[1][0]
                    distance = m.sqrt(x*x + y*y)
                elif AB_AE < 0:
                    y = self.bullet.y - line[0][1]
                    x = self.bullet.x - line[0][0]
                    distance = m.sqrt(x*x + y*y)
                else:
                    x1 = AB[0]
                    y1 = AB[1]  
                    x2 = AE[0]
                    y2 = AE[1]
                    mod = m.sqrt(x1 * x1 + y1 * y1);  
                    distance = abs(x1 * y2 - y1 * x2) / mod
                if distance <= self.radius:
                    if line[0][0] == line[1][0]:
                        self.bullet.deg = - self.bullet.deg
                    else :
                        self.bullet.deg = 180 - self.bullet.deg
                    return 'done'

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
        p.draw.rect(win, (0, 0, 0), self.dim)


tank = player(200, 200, 64, 64)
enemy = player(100, 100, 40, 40)
enemyt = True
bullets = []
clock = p.time.Clock()
wallt = True
walls = []
wall = obstructions()

while run:
    p.time.delay(35)
    clock.tick(120)
    
    for b in bullets:
        x = b.bounce(b, walls)

        if b.y < 700 and b.y > 0 and b.x > 0 and b.x < 1000:
            b.y -= round(m.cos(((m.pi)/180) * b.deg ) * b.vel)
            b.x += round(m.sin(((m.pi)/180) * b.deg) * b.vel)
        else :
            bullets.pop(bullets.index(b))
        '''if round(((enemy.y - b.y)**2 + (enemy.x - b.x)**2)**(1/2)) <= enemy.radius:
            enemyt = False'''


    if wallt:
        for i in range(25):
            a = obstructions()
            walls.append(a)
            if tank.dim.colliderect(a.dim):
                walls.remove(a)
        wallt = False
             

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    keys = p.key.get_pressed()

    if keys[p.K_UP]:
        tempx = tank.x
        tempy = tank.y
        tank.y -= round(m.cos(((m.pi)/180) * tank.deg ) * tank.vel)
        tank.dim[1] = tank.y
        if tank.movementcheck(tank, walls) == 'n':
            tank.y = tempy
        tank.x += round(m.sin(((m.pi)/180) * tank.deg) * tank.vel)
        tank.dim[0] = tank.x
        if tank.movementcheck(tank, walls) == 'n':
            tank.x = tempx
    if keys[p.K_DOWN]:
        tempx = tank.x
        tempy = tank.y
        tank.y += round(m.cos(((m.pi)/180) * tank.deg ) * tank.vel)
        tank.dim[1] = tank.y
        if tank.movementcheck(tank, walls) == 'n':
            tank.y = tempy
        tank.x -= round(m.sin(((m.pi)/180) * tank.deg) * tank.vel)
        tank.dim[0] = tank.x
        if tank.movementcheck(tank, walls) == 'n':
            tank.x = tempx

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

    win.fill((0, 255, 0))
    for wal in walls:
        wal.animate(win)
    for bullet in bullets:
        bullet.animate(win)
    tank.animate(win)
    if enemyt :
        p.draw.rect(win, (0, 155, 0), (enemy.x, enemy.y, enemy.width, enemy.height))
    
    p.display.flip()

p.quit()
