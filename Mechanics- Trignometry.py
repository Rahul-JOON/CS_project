import pygame as p
import math as m

p.init()
win = p.display.set_mode((500, 500))
p.display.set_caption("Mechanics")
x = 200
y = 200
radius = 40
vel = 15
deg = 0
slantness = 0

run = True

while run:
    p.time.delay(50)

    print((x, y), round(m.sin(deg) * vel), m.cos(deg) * vel, deg)

    if deg > 360:
        deg = 1
    elif deg < 0:
        deg = 359

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    keys = p.key.get_pressed()

    if keys[p.K_UP]:
        y -= round(m.cos(((m.pi)/180) * deg ) * vel)
        x += round(m.sin(((m.pi)/180) * deg) * vel)
    if keys[p.K_DOWN]:
        y += round(m.cos(((m.pi)/180) * deg) * vel)
        x -= round(m.sin(((m.pi)/180) * deg) * vel)

    if keys[p.K_RIGHT]:
        deg += 15
    if keys[p.K_LEFT]:
        deg -= 15

    win.fill((0, 0, 0))
    p.draw.circle(win, (155, 0, 0), (x,y), radius)
    p.display.update()

p.quit()