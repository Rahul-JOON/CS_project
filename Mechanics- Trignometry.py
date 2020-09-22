import pygame as p
import math as m

p.init()

win = p.display.set_mode((1000, 700))
p.display.set_caption("GUNMAN")

run = True

class player():
    def __init__(self, x , y, radius):
        self.x = x 
        self.y = y
        self.radius = radius
        self.vel = 15
        self.deg = 0
        self.slantness = 0
    
class gun():
    def __init__(self, x, y, radius, deg):
        self.x = x 
        self.y = y 
        self.radius = radius 
        self.deg = deg
        self.vel = 10
    def animate(self, win):
        p.draw.circle(win, (255 ,255, 255), (self.x, self.y), self.radius)


tank = player(200, 200, 40)
enemy = player(100, 100, 40)
enemyt = True
bullets = []
clock = p.time.Clock()

while run:
    p.time.delay(50)
    clock.tick(60)
    print(tank.deg)


    for b in bullets:
        if b.y < 700 and b.y > 0 and b.x > 0 and b.x < 1000:
            b.y -= round(m.cos(((m.pi)/180) * b.deg ) * b.vel)
            b.x += round(m.sin(((m.pi)/180) * b.deg) * b.vel)
        else :
            bullets.pop(bullets.index(b))
        if round(((enemy.y - b.y)**2 + (enemy.x - b.x)**2)**(1/2)) <= enemy.radius:
            enemyt = False

    if tank.deg == 360:
        tank.deg = 0
    elif tank.deg < 0:
        tank.deg = 345

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
        bullets.append(gun(tank.x, tank.y, 10, tank.deg))

    win.fill((0, 0, 0))
    p.draw.circle(win, (155, 0, 0), (tank.x, tank.y), tank.radius)
    if enemyt :
        p.draw.circle(win, (0, 155, 0), (enemy.x, enemy.y), enemy.radius)
    for bullet in bullets:
        bullet.animate(win)
    p.display.update()

p.quit()