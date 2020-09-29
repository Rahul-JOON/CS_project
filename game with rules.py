import pygame as p
import math as m
import os
from sympy import symbols, Eq, solve 
from collections import defaultdict

p.init()

win = p.display.set_mode((1400, 720))
p.display.set_caption("Tank Busters")
linesinquads = [[()], [], [], []]

run = True

def quadcheck(qx, qy):
        #self.qx = qx
        #self.qy = qy
        if qx < 700 and qy < 360:
            quad = 0
        elif qx >= 700 and qy < 360:
            quad = 1
        elif qx < 700 and qy >= 360:
            quad = 2
        else :
            quad = 3
        return quad

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
    
class rules():
    def __init__(self):
        self.x, self.y = symbols('x y')

    def tank(self, tx, ty, cx, cy):
        self.tx = tx
        self.ty = ty
        self.cx = cx
        self.cy = cy
        self.q = quadcheck(self.tx, self.ty)
        for i in linesinquads[self.q]:
            eq1 = Eq(self.y - 500, 0)
            eq2 = Eq(((self.y - self.ty) * (self.cx))/(self.cy) * (self.x - self.tx), 0)
            sol = solve((eq1, eq2), (self.x, self.y))
            sol = defaultdict(lambda: 0, sol)
            pi = (sol[self.x], sol[self.y])
            print(round(((pi[1] - self.ty + 64)**2 + (pi[0] - self.tx + 64)**2)**(1/2)))
            if round(((pi[1] - self.ty + 64)**2 + (pi[0] - self.tx + 64)**2)**(1/2)) <= 90:
                return 'n'
        return 'y'

tank = player(200, 200, 40)
enemy = player(100, 100, 40)
enemyt = True
bullets = []
clock = p.time.Clock()

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


    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    keys = p.key.get_pressed()

    if keys[p.K_UP]:
        cx = round(m.sin(((m.pi)/180) * tank.deg) * tank.vel)
        cy = -(round(m.cos(((m.pi)/180) * tank.deg ) * tank.vel))
        if tank.x > 0 and tank.x < 1564:
            if tank.y > 0 and tank.y < 784:
                if rules().tank(tank.x, tank.y, cx, cy) == 'y':
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

    win.blit(p.image.load(os.path.join('Resources', 'bg.png')).convert() ,(0, 0))
    #p.draw.circle(win, (155, 0, 0), (tank.x, tank.y), tank.radius)
    for bullet in bullets:
        bullet.animate(win)
    tank.animate(win)
    if enemyt :
        p.draw.circle(win, (0, 155, 0), (enemy.x, enemy.y), enemy.radius)
    
    p.display.update()

p.quit()