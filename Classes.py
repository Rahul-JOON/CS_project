import socket
import pygame as p
import random as r
import math as m
import os

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
                p.draw.circle(win, (0 ,0, 0), (self.x, self.y), self.radius)

class obstructions():
            def __init__(self):
                self.x = r.randint(0, 1436)
                self.y = r.randint(0, 700)
                self.width = r.randint(30, 64)
                self.height = r.randint(30, 128)
                self.dim = (self.x, self.y, self.width, self.height)

            def animate(self, win):
                p.draw.rect(win, (0, 0, 0), self.dim)

class Networking():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.1.105'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.answer = self.connect()

    def connect(self):
        try :
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            print("error in sending")
    
    def send(self, data):
        try :
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as s:
            print(s)                       