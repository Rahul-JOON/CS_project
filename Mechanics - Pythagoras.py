import pygame as p

p.init()
win = p.display.set_mode((500, 500))
p.display.set_caption("Mechanics")
x = 200
y = 200
radius = 40
vel = 5
deg = 0
slantness = 0

run = True

while run:
    p.time.delay(50)

    print((x, y), ((vel ** 2) - (slantness ** 2)) ** 0.5, deg)

    if deg > 36:
        deg = 1
    elif deg < 0:
        deg = 35

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    keys = p.key.get_pressed()

    if keys[p.K_UP]:
        if deg >=0 and deg <= 9:
            slantness = deg * 0.555555
            y -= int(((vel**2) - (slantness**2))**0.5)
            x += int(slantness)
        elif deg > 9 and deg <= 18:
            slantness = (deg - 9) * 0.555555
            x += int(((vel ** 2) - (slantness ** 2)) ** 0.5)
            y += int(slantness)
        elif deg > 18 and deg <= 27:
            slantness = (deg - 18) * 0.555555
            y += int(((vel**2) - (slantness**2))**0.5)
            x -= int(slantness)
        elif deg > 27 and deg <= 36:
            slantness = (deg - 27) * 0.555555
            y -= int(slantness)
            x -= int(((vel**2) - (slantness**2))**0.5)
    if keys[p.K_DOWN]:
        if deg >= 0 and deg <= 9:
            slantness = deg * 0.555555
            y += int(((vel**2) - (slantness**2))**0.5)
            x -= int(slantness)
        elif deg > 9 and deg <= 18:
            slantness = (deg - 9) * 0.555555
            x -= int(((vel ** 2) - (slantness ** 2)) ** 0.5)
            y -= int(slantness)
        elif deg > 18 and deg <= 27:
            slantness = (deg - 18) * 0.555555
            y -= int(((vel**2) - (slantness**2))**0.5)
            x += int(slantness)
        elif deg > 27 and deg <= 36:
            slantness = (deg - 27) * 0.555555
            y += int(slantness)
            x += int(((vel ** 2) - (slantness ** 2)) ** 0.5)
    if keys[p.K_RIGHT]:
        deg += 1
    if keys[p.K_LEFT]:
        deg -= 1

    win.fill((0, 0, 0))
    p.draw.circle(win, (155, 0, 0), (x,y), radius)
    p.display.update()

p.quit()