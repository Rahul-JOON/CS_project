from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
import imageio
from pathlib import Path
import pygame as p
import random as r
import math as m
import os
global player1_score
global player2_score
player1_score=0
player2_score=0


p.mixer.init()

p.mixer.music.load("battle.mp3")
p.mixer.music.play(loops=2)
p.mixer.music.set_volume(0.05)

root=Tk()
root.title("TankBusters")
root.iconbitmap('tank.ico')
root.geometry("1280x720")
root.configure(bg="brown")
# The video which plays during the beginning
def startup():    
    top=Toplevel()
    top.title("TankBusters")
    top.iconbitmap('tank.ico')
    my_label=Label(top)
    my_label.grid(row=0,column=0)
    video_name= 'starting.mp4'
    video=imageio.get_reader(video_name)
    delay = int(1000 / video.get_meta_data()['fps'])


    def stream(label):
        try:
            image=video.get_next_data()
        except:
            video.close()
            return
        root.iconify()    
        label.after(delay,lambda:stream(label))
        frame_image=ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

    my_label.after(delay,lambda:stream(my_label))
    root.deiconify()
    my_label.after(25000,lambda:top.destroy())
    root.deiconify()

def menu_page():
    
    
    global img
    global img2
    global img3
    global img4
        
    img=ImageTk.PhotoImage(Image.open('start .png'))
    global Play_button
    Play_button=Button(image=img,command=start,padx=5)
    Play_button.configure(highlightthickness=0)    
    Play_button.grid(row=0,column=6)

    img2=ImageTk.PhotoImage(Image.open("tanki.png"))
    global menulbl
    menulbl=Label(image=img2)
    menulbl.grid(row=0,column=0,rowspan=5,columnspan=1)

    img3=ImageTk.PhotoImage(Image.open("settings.png"))
    global settings_button
    settings_button=Button(image=img3,command=settings,padx=1)
    settings_button.configure(highlightthickness=0)
    settings_button.grid(row=1,column=6)

    img4=ImageTk.PhotoImage(Image.open("exit.png"))
    global exit_button
    exit_button=Button(image=img4,command=exit1,padx=5)
    exit_button.configure(highlightthickness=0)
    exit_button.grid(row=2,column=6)
    
# The function of the start button    
def start():
    menulbl.destroy()
    
    Play_button.destroy()
    settings_button.destroy()
    exit_button.destroy()
    

    # Game to start in this function
    
        
    def MAIN_GAME(player1_score,player2_score):
        def END_GAME(player1_score,player2_score):
           
            def menu():
                root=Tk()
                root.title("TankBusters")
                root.iconbitmap('tank.ico')
                root.geometry("1280x720")
                root.configure(bg="brown")
                menu_page()
            def quitz():
                top2.destroy()

            def again():
                top2.destroy()
                MAIN_GAME(player1_score,player2_score)    
            top2=Tk()
            top2.title("TankBusters")
            top2.iconbitmap('tank.ico')
            top2.configure(bg="brown")
            global imgend
            imgend=ImageTk.PhotoImage(Image.open("score.png"))
            labelre=Label(top2,image=imgend)
            labelre.grid(row=0,column=0,rowspan=2,columnspan=6)
                
            if tank1y==False:
                player2_score+=1
            if tank2y==False:
                player1_score+=1

            myFont = font.Font(family='Helvetica', size=40, weight='bold')
            img1score=ImageTk.PhotoImage(Image.open("player 1 score.png"))
            score1=Label(image=img1score)
            score1.grid(row=3,column=1)
            score11=Label(text=player1_score)
            score11.grid(row=4,column=1)
            score11['font'] = myFont
            img2score=ImageTk.PhotoImage(Image.open("player 2 score.png"))

            score2=Label(image=img2score)
            score2.grid(row=3,column=3)
            score22=Label(text=player2_score)
            score22['font'] = myFont
            score22.grid(row=4,column=3)
                
            imgagain=ImageTk.PhotoImage(Image.open("play again.png"))
            play_again=Button(top2,image=imgagain,command=again)
            play_again.grid(row=5,column=2)
                
            imgquitm=ImageTk.PhotoImage(Image.open("quit menu.png"))
            Quit_menu=Button(top2,image=imgquitm,command=menu)
            Quit_menu.grid(row=6,column=1)
                
            imgquitd=ImageTk.PhotoImage(Image.open("quit desktop.png"))
            play_again=Button(top2,image=imgquitd,command=quitz)
            play_again.grid(row=6,column=3)

                
            top2.mainloop()
        

        p.init()

        win = p.display.set_mode((1100, 700))
        p.display.set_caption("TankBusters")
        win.fill((255,255,255))
        run = True
        def newcolor():
            colorcodes = r.randint(0, 255)
            return colorcodes

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
                win.blit(p.image.load(os.path.join('Resources', f'tr{self.deg}.png')).convert() , (self.x, self.y) )
            
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


        tank1 = player(200, 200, 64, 64)
        global tank1y
        tank1y=True
        tank2 = player(200, 200, 64, 64)
        global tank2y
        tank2y=True
        
        bullets1 = []
        bullets2 = []
        clock = p.time.Clock()
        wallt = True
        walls = []
        wall = obstructions()


        while run:
            p.time.delay(35)
            clock.tick(120)
            
            for b1 in bullets1:
                x = b1.bounce(b1, walls)

                if b1.y < 700 and b1.y > 0 and b1.x > 0 and b1.x < 1000:
                    b1.y -= round(m.cos(((m.pi)/180) * b1.deg ) * b1.vel)
                    b1.x += round(m.sin(((m.pi)/180) * b1.deg) * b1.vel)
                else :
                    bullets1.pop(bullets1.index(b1))
                if round(((tank2.y - b1.y)**2 + (tank2.x - b1.x)**2)**(1/2)) <= tank2.width:
                    tank2y=False
                    
            for b2 in bullets2:
                x = b2.bounce(b2, walls)

                if b2.y < 700 and b2.y > 0 and b2.x > 0 and b2.x < 1000:
                    b2.y -= round(m.cos(((m.pi)/180) * b2.deg ) * b2.vel)
                    b2.x += round(m.sin(((m.pi)/180) * b2.deg) * b2.vel)
                else :
                    bullets2.pop(bullets2.index(b2))        
                if round(((tank1.y - b2.y)**2 + (tank1.x - b2.x)**2)**(1/2)) <= tank1.width:
                    tank1y=False
                    


            if wallt:
                for i in range(50):
                    a = obstructions()
                    walls.append(a)
                    if tank1.dim.colliderect(a.dim):
                        walls.remove(a)
                        
                wallt = False
                     

            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
                    
            keys = p.key.get_pressed()

            if keys[p.K_UP]:
                tempx1 = tank1.x
                tempy1 = tank1.y
                tank1.y -= round(m.cos(((m.pi)/180) * tank1.deg ) * tank1.vel)
                tank1.dim[1] = tank1.y
                if tank1.movementcheck(tank1, walls) == 'n':
                    tank1.y = tempy1
                tank1.x += round(m.sin(((m.pi)/180) * tank1.deg) * tank1.vel)
                tank1.dim[0] = tank1.x
                if tank1.movementcheck(tank1, walls) == 'n':
                    tank1.x = tempx1
            if keys[p.K_DOWN]:
                tempx1 = tank1.x
                tempy1 = tank1.y
                tank1.y += round(m.cos(((m.pi)/180) * tank1.deg ) * tank1.vel)
                tank1.dim[1] = tank1.y
                if tank1.movementcheck(tank1, walls) == 'n':
                    tank1.y = tempy1
                tank1.x -= round(m.sin(((m.pi)/180) * tank1.deg) * tank1.vel)
                tank1.dim[0] = tank1.x
                if tank1.movementcheck(tank1, walls) == 'n':
                    tank1.x = tempx1

            if keys[p.K_RIGHT]:
                tank1.deg += 15
            if keys[p.K_LEFT]:
                tank1.deg -= 15

            if keys[p.K_SPACE]:
                bullets1.append(gun(tank1.x + 32, tank1.y + 32, 5, tank1.deg))

            if keys[p.K_w]:
                tempx2 = tank2.x
                tempy2 = tank2.y
                tank2.y -= round(m.cos(((m.pi)/180) * tank2.deg ) * tank2.vel)
                tank2.dim[1] = tank2.y
                if tank2.movementcheck(tank2, walls) == 'n':
                    tank2.y = tempy2
                tank2.x += round(m.sin(((m.pi)/180) * tank2.deg) * tank2.vel)
                tank2.dim[0] = tank2.x
                if tank2.movementcheck(tank2, walls) == 'n':
                    tank2.x = tempx2
            if keys[p.K_s]:
                tempx2 = tank2.x
                tempy2= tank2.y
                tank2.y += round(m.cos(((m.pi)/180) * tank2.deg ) * tank2.vel)
                tank2.dim[1] = tank2.y
                if tank2.movementcheck(tank2, walls) == 'n':
                    tank2.y = tempy2
                tank2.x -= round(m.sin(((m.pi)/180) * tank2.deg) * tank2.vel)
                tank2.dim[0] = tank2.x
                if tank2.movementcheck(tank2, walls) == 'n':
                    tank2.x = tempx2

            if keys[p.K_d]:
                tank2.deg += 15
            if keys[p.K_a]:
                tank2.deg -= 15

            if keys[p.K_f]:
                bullets2.append(gun(tank2.x + 32, tank2.y + 32, 5, tank2.deg))    
            
            if tank1.deg == 360:
                tank1.deg = 0
            elif tank1.deg < 0:
                tank1.deg = 345
            if tank2.deg == 360:
                tank2.deg = 0
            elif tank2.deg < 0:
                tank2.deg = 345    

            win.fill((255, 229, 180))
            for wal in walls:
                wal.animate(win)
            for bullet1 in bullets1:
                bullet1.animate(win)
            for bullet2 in bullets2:
                bullet2.animate(win)    
            tank1.animate(win)
            tank2.animate(win)
            if tank1y==False :
                p.draw.rect(win, (0, 155, 0), (tank1.x, tank1.y, tank1.width, tank1.height))
                
                run = False
            
            if tank2y==False :
                p.draw.rect(win, (0, 155, 0), (tank2.x, tank2.y, tank2.width, tank2.height))
                
                run=False
                
            
            p.display.flip()

        p.quit()
        

        
        END_GAME(player1_score,player2_score)
    def color2():
        tanklabel1.destroy()
        tanker_name1.destroy()
        submit1.destroy()
        start.destroy()
        if tank_color1=="red":        
            showcolor1.destroy()
        if tank_color1=="blue":
            showcolor2.destroy()
        if tank_color1=="green":
            showcolor3.destroy()
        if tank_color1=="white":
            showcolor4.destroy()
        if tank_color1=="yellow":
            showcolor5.destroy()

        def name2():
            choice2.destroy()
            blue2.destroy()
            red2.destroy()
            green2.destroy()
            white2.destroy()
            yellow2.destroy()
            start1.destroy()
            colorsee2.destroy()

            def namesub2():
                player_name2=tanker_name2.get()
            def GAME():
                 
                
                root.destroy()
                MAIN_GAME(0,0)    
            
            
            global imgt2
            imgt2=ImageTk.PhotoImage(Image.open("name2.png"))
            global tanklabel1
            tanklabel11=Label(image=imgt2)
            tanklabel11.grid(row=0,column=0,rowspan=2,columnspan=9,padx=200)
            tanklabel11.configure(highlightthickness=0)

            global tanker_name2
            tanker_name2=Entry(root,width=60)
            tanker_name2.grid(row=4,column=4,pady=100)

            global imgs2
            imgs2=ImageTk.PhotoImage(Image.open("submit.png"))
            global submit1
            submit2=Button(root,image=imgs2,command=namesub2)
            submit2.grid(row=6,column=4)

            global imgst2
            imgst2=ImageTk.PhotoImage(Image.open("start game.png"))
            global start
            start2=Button(root,image=imgst2,command=GAME)
            start2.grid(row=6,column=7)
            
            
        global tank_color2
        color2=""
        def colorz2(color2):
            global tank_color2
            tank_color2=color2
            
        
        def color22():
            if tank_color2=="red":        
                global imgr2
                imgr2=ImageTk.PhotoImage(Image.open("red.png"))
                global showcolor11
                showcolor11=Label(image=imgr2)
                showcolor11.grid(row=5,column=2)
            if tank_color2=="blue":
                global imgb2
                imgb2=ImageTk.PhotoImage(Image.open("blue.png"))
                global showcolor22
                showcolor22=Label(image=imgb2)
                showcolor22.grid(row=5,column=2)
            if tank_color2=="green":
                global imgg2
                imgg2=ImageTk.PhotoImage(Image.open("green.png"))
                global showcolor33
                showcolor33=Label(image=imgg2)
                showcolor33.grid(row=5,column=2)
            if tank_color2=="white":
                global imgw2
                imgw2=ImageTk.PhotoImage(Image.open("white.png"))
                global showcolor44
                showcolor44=Label(image=imgw2)
                showcolor44.grid(row=5,column=2)
            if tank_color2=="yellow":
                global imgy2
                imgy2=ImageTk.PhotoImage(Image.open("yellow.png"))
                global showcolor55
                showcolor55=Label(image=imgy2)
                showcolor55.grid(row=5,column=2)
                
        global imgx2
        imgx2=ImageTk.PhotoImage(Image.open("player2.png"))
        choice2=Label(image=imgx2)
        choice2.grid(row=0,column=0,rowspan=2,columnspan=9,padx=200)

        blue2=Button(root,bg="blue",width=20,height=10,command=lambda:colorz2("blue"))
        blue2.grid(row=3,column=1,pady=5)

        red2=Button(root,bg="red",width=20,height=10,command=lambda:colorz2("red"))
        red2.grid(row=3,column=4,pady=5)

        green2=Button(root,bg="green",width=20,height=10,command=lambda:colorz2("green"))
        green2.grid(row=3,column=7,pady=5)

        white2=Button(root,bg="white",width=20,height=10,command=lambda:colorz2("white"))
        white2.grid(row=4,column=2,pady=30)

        yellow2=Button(root,bg="yellow",width=20,height=10,command=lambda:colorz2("yellow"))
        yellow2.grid(row=4,column=5,pady=30)

        global imgchosen2
        imgchosen2=ImageTk.PhotoImage(Image.open("see color chosen.png"))
        colorsee2=Button(root,image=imgchosen,command=color22)
        colorsee2.grid(row=5,column=1)
        global imgst2
        imgst2=ImageTk.PhotoImage(Image.open("next.png"))
        start1=Button(root,image=imgst2,command=name2)
        start1.grid(row=5,column=7)

        
        
    def namesub1():
        player_name1=tanker_name1.get()

    def name():
        choice.destroy()
        blue.destroy()
        red.destroy()
        green.destroy()
        white.destroy()
        yellow.destroy()
        next1.destroy()
        colorsee.destroy()
        
        
        global imgt
        imgt=ImageTk.PhotoImage(Image.open("name1.png"))
        global tanklabel1
        tanklabel1=Label(image=imgt)
        tanklabel1.grid(row=0,column=0,rowspan=2,columnspan=9,padx=200)
        tanklabel1.configure(highlightthickness=0)

        global tanker_name1
        tanker_name1=Entry(root,width=60)
        tanker_name1.grid(row=4,column=4,pady=100)

        global imgs
        imgs=ImageTk.PhotoImage(Image.open("submit.png"))
        global submit1
        submit1=Button(root,image=imgs,command=namesub1)
        submit1.grid(row=6,column=4)

        global imgst
        imgst=ImageTk.PhotoImage(Image.open("next.png"))
        global start
        start=Button(root,image=imgst,command=color2)
        start.grid(row=6,column=7)
        
    global tank_color1
    
    tank_color1=str()
    color1=""
    def colorz(color1):
        global tank_color1
        tank_color1=color1
    
    root.configure(bg="brown")
    # Text for choice of color
    global imgx
    imgx=ImageTk.PhotoImage(Image.open("player1.png"))
    choice=Label(image=imgx)
    choice.grid(row=0,column=0,rowspan=2,columnspan=9,padx=200)


    # Option buttons for all the colors
    blue=Button(root,bg="blue",width=20,height=10,command=lambda:colorz("blue"))
    blue.grid(row=3,column=1,pady=5)

    red=Button(root,bg="red",width=20,height=10,command=lambda:colorz("red"))
    red.grid(row=3,column=4,pady=5)

    green=Button(root,bg="green",width=20,height=10,command=lambda:colorz("green"))
    green.grid(row=3,column=7,pady=5)

    white=Button(root,bg="white",width=20,height=10,command=lambda:colorz("white"))
    white.grid(row=4,column=2,pady=30)

    yellow=Button(root,bg="yellow",width=20,height=10,command=lambda:colorz("yellow"))
    yellow.grid(row=4,column=5,pady=30)

    root.update()

    def color():
        if tank_color1=="red":        
            global imgr
            imgr=ImageTk.PhotoImage(Image.open("red.png"))
            global showcolor1
            showcolor1=Label(image=imgr)
            showcolor1.grid(row=5,column=2)
        if tank_color1=="blue":
            global imgb
            imgb=ImageTk.PhotoImage(Image.open("blue.png"))
            global showcolor2
            showcolor2=Label(image=imgb)
            showcolor2.grid(row=5,column=2)
        if tank_color1=="green":
            global imgg
            imgg=ImageTk.PhotoImage(Image.open("green.png"))
            global showcolor3
            showcolor3=Label(image=imgg)
            showcolor3.grid(row=5,column=2)
        if tank_color1=="white":
            global imgw
            imgw=ImageTk.PhotoImage(Image.open("white.png"))
            global showcolor4
            showcolor4=Label(image=imgw)
            showcolor4.grid(row=5,column=2)
        if tank_color1=="yellow":
            global imgy
            imgy=ImageTk.PhotoImage(Image.open("yellow.png"))
            global showcolor5
            showcolor5=Label(image=imgy)
            showcolor5.grid(row=5,column=2)    
       
    
    global imgz
    imgz=ImageTk.PhotoImage(Image.open("Next.png"))
    next1=Button(root,image=imgz,command=name)
    next1.configure(highlightthickness=0)
    next1.grid(row=5,column=7)
    global imgchosen
    imgchosen=ImageTk.PhotoImage(Image.open("see color chosen.png"))
    colorsee=Button(root,image=imgchosen,command=color)
    colorsee.grid(row=5,column=1)
    
    root.configure(bg="brown")
    root.update()
# The function of the settings button
def settings():
    
    Play_button.destroy()
    settings_button.destroy()
    exit_button.destroy()
    
    var1=StringVar()
    var2=IntVar()
    
    global imgA
    imgA=ImageTk.PhotoImage(Image.open("settings.png"))    
    setting=Label(image=imgA)
    setting.grid(row=0,column=6)

    def back():
        menulbl.destroy()
        musicon.destroy()
        musicoff.destroy()
        setting.destroy()
        back_button.destroy()
        menu_page()

    def play():
        p.mixer.music.load("battle.mp3")
        p.mixer.music.play(loops=2)
        p.mixer.music.set_volume(0.05)

    def stop():
        p.mixer.music.stop()
    global imgm1
    imgm1=ImageTk.PhotoImage(Image.open("music on.png"))
    musicon=Button(root,image=imgm1,command=play)  
    musicon.grid(row=1,column=6)

    global imgm2
    imgm2=ImageTk.PhotoImage(Image.open("music off.png"))
    musicoff=Button(root,image=imgm2,command=stop)  
    musicoff.grid(row=2,column=6)
    root.update()
        
    
    
    global imgB
    imgB=ImageTk.PhotoImage(Image.open("back.png"))
    back_button=Button(root,image=imgB,command=back)
    back_button.configure(highlightthickness=0)
    back_button.grid(row=4,column=6)

# The function of the exit button
def exit1():
    root.destroy()

# The function for the main menu consisting of start, settings and exit buttons. 


# All executions
menu_page()
root.iconify()

root.deiconify()









root.mainloop()

