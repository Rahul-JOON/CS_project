import pygame as p
import math as m

p.init()

win = p.display.set_mode((500, 500))
p.display.set_caption("Mechanics")

run = True

class player():
    def __init__(self, x , y, radius):
        self.x = x 
        self.y = y
        self.radius = radius
        self.vel = 15
        self.deg = 0
        self.slantness = 0

tank = player(200, 200, 40)

while run:
    p.time.delay(50)

    print((tank.x, tank.y), round(m.sin(tank.deg) * tank.vel), m.cos(tank.deg) * tank.vel, tank.deg)

    if tank.deg > 360:
        tank.deg = 1
    elif tank.deg < 0:
        tank.deg = 359

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

    win.fill((0, 0, 0))
    p.draw.circle(win, (155, 0, 0), (tank.x, tank.y), tank.radius)
    p.display.update()

p.quit()