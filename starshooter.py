'''
                                 _                      _                 
                                (_)                    | |                
  ___ ____  _____  ____ _____    _ ____ _   _ _____  __| |_____  ____ ___ 
 /___)  _ \(____ |/ ___) ___ |  | |  _ \ | | (____ |/ _  | ___ |/ ___)___)
|___ | |_| / ___ ( (___| ____|  | | | | \ V // ___ ( (_| | ____| |  |___ |
(___/|  __/\_____|\____)_____)  |_|_| |_|\_/ \_____|\____|_____)_|  (___/ 
     |_|                                                                  

'''


import turtle as t
import random

px, py = 0, 0
ax, ay = 9999, 9999
ex, ey = 0, 100
shot = 0
alive = 1
timera = 0
enemiesc = 5
total = 0
kills = 0
rows = 3
level = 0
menu = 1
t.bgcolor("black")
t.title("starshooter")
enemies = []
for __ in range(rows):
    for _ in range(enemiesc):
        enemies.append({
            "ex": -100 + _ * 50,
            "ey": 200 + __ * 20,
            "alive": 1,
            "timera": 0
        })
        total += 1
t.tracer(0, 0)
t.penup()
t.hideturtle()

def menu1():
    if menu == 1:
        t.goto(-100, 0)
        t.pencolor("red")
        t.write("SPACE SHOOTER\n        press [space] to start", font=("Arial", 16, "normal"))
    if menu == 0:
        mainloop()


menu1()

def player():
    t.pencolor("black")
    t.fillcolor("gray")
    t.goto(px, py)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(30)
        t.right(90)
    t.end_fill()
    t.forward(7.5)
    t.begin_fill()
    for _ in range(4):
        t.forward(15)
        t.left(90)
    t.end_fill()
    t.penup()

def shoot():
    global menu
    if menu == 1:
        menu = 0
        menu1()
    else:
        t.pencolor("black")
        t.fillcolor("orange")
        global ax, ay, shot
        ay = py
        ax = px + 15
        t.goto(ax, ay)
        t.pendown()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.penup()
        shot = 1

def movebullet():
    t.fillcolor("orange")
    global ay, shot
    t.goto(ax, ay)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    
    if shot == 1:
        ay += 10
    if ay > 300:
        shot = 0
        ay = 9999
def gameover():
    t.clear()
    t.goto(0, 0)
    t.color("red")
    t.write("GAME OVER", align="center",font=("Arial", 20, "normal"))

def nextlevel():
    global total, enemiesc, rows, level
    total = 0
    level += 1
    if enemiesc < 8:
        enemiesc += 1
    if rows < 10:
        rows += 1
    for __ in range(rows):
        for _ in range(enemiesc):
            enemies.append({
                "ex": -100 + _ * 50,
                "ey": 200 + __ * 20,
                "alive": 1,
                "timera": 0
            })
            total += 1
        



def enemy():
    t.pencolor("black")
    global shot, ay, alive, kills
    for _ in enemies:
        if _["alive"] == 1:
            t.goto(_["ex"], _["ey"])
            t.pendown()
            t.fillcolor("green")
            t.begin_fill()
            t.circle(10)
            t.end_fill()
            t.penup()
            if _["timera"] < (30 - level):
                _["timera"] += 1
            elif _["timera"] == (30 - level):
                _["ey"] -= 10
                _["timera"] = 0
            if ay == _["ey"] and (ax - 15) == _["ex"]:
                _["alive"] = 0

            if _["ey"] < 0:
                gameover()
    
        
def text():
    t.goto(-100, -100)
    t.pencolor("white")
    t.write(f"level {level}", font=("Arial", 10, "normal"))
        

starpos = []
starc = 50
for _ in range(starc):
    starpos.append({
        "sx": random.randint(-300, 300),
        "sy": random.randint(-300, 300)
    })

def stars():
    for _ in starpos:
        t.goto(_["sx"], _["sy"])
        t.pencolor("white")
        t.fillcolor("white")
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()

def left():
    global px
    px -= 50

def right():
    global px
    px += 50

def click(x, y):
    global menu
    if menu == 1:
        menu = 0
        menu1()
    if menu == 0:
        if 0 < y:
            shoot()
        if 0 < x and y < 0:
            right()
        if x < 0 and y < 0:
            left()

t.onkey(left, "a")
t.onkey(right, "d")
t.onkey(shoot, "space")
t.onscreenclick(click)
t.listen()
def mainloop():
    t.clear()

    stars()
    text()
    movebullet()
    enemy()
    player()


    if all(_["alive"] == 0 for _ in enemies):
        nextlevel()

    
    t.update()

    t.ontimer(mainloop, 30)


t.mainloop()
