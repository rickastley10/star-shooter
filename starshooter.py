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

px, py = 0, 0
ax, ay = 9999, 9999
ex, ey = 0, 100
shot = 0
alive = 1
timera = 0
enemiesc = 5
enemies = []
for _ in range(enemiesc):
    enemies.append({
        "ex": -100 + _ * 50,
        "ey": 200,
        "alive": 1,
        "timera": 0
    })
t.tracer(0, 0)
t.penup()
t.hideturtle()
def player():
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
    t.write("GAME OVER")

def enemy():
    global shot, ay, alive
    for _ in enemies:
        if _["alive"] == 1:
            t.goto(_["ex"], _["ey"])
            t.pendown()
            t.fillcolor("green")
            t.begin_fill()
            t.circle(10)
            t.end_fill()
            t.penup()
            if _["timera"] < 10:
                _["timera"] += 1
            elif _["timera"] == 10:
                _["ey"] -= 10
                _["timera"] = 0
            if ay == _["ey"] and (ax - 15) == _["ex"]:
                _["alive"] = 0

            if _["ey"] < 0:
                gameover()

        

def left():
    global px
    px -= 50

def right():
    global px
    px += 50


t.onkey(left, "a")
t.onkey(right, "d")
t.onkey(shoot, "space")
t.listen()
def mainloop():
    t.clear()
    movebullet()
    enemy()
    player()

    t.update()

    t.ontimer(mainloop, 30)

mainloop()
t.mainloop()