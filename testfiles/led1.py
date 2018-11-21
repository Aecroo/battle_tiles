from ptpulse import ledmatrix
import time
import random

ledmatrix.rotation(0)
ledmatrix.clear()

class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.farbe = 0, 0, 0
        self.show = True
    
    def getx(self):
        return self.x

    def setx(self, wert):
        self.x = wert
        
    def gety(self):
        return self.y
        
    def sety(self, wert):
        self.y = wert
    
    def getfarbe(self):
        return self.farbe
    
    def getshow(self):
        return self.show
        
    def setshow(self, wert):
        self.show = wert
    
    def setfarbe(self,r,g,b):
        self.farbe = r,g,b

def showmap(r, g, b):
    for x in range(0, 7):
        for y in range(0, 7):
            rr = int(r)
            gg = int(g)
            bb = int(b)
            ledmatrix.set_pixel(x, y, rr, gg, bb)

def moveplayer():
    i = random.randint(1,4)
    if i == 1: x, y = 1, 0
    elif i == 2: x, y = 0, 1
    elif i == 3: x, y = -1, 0
    else: x, y = 0, -1
    
    return x,y

def clear():
    ledmatrix.clear()
    ledmatrix.show()
    
def rndplayer():
    player1[0] = random.randint(0,6)
    player1[1] = random.randint(0,6)
    print(player1)
    ledmatrix.set_pixel(player1[0], player1[1], 0, 255, 255)

def loop(ini):
    if ini.getx() is 1 and ini.gety() != 5:
        ini.sety(ini.gety() + 1)
        ledmatrix.set_pixel(ini.getx(),ini.gety(),ini.getfarbe()[0],ini.getfarbe()[1],ini.getfarbe()[2])
        pass
        
    elif ini.gety() is 5 and ini.getx() != 5:
        ini.setx(ini.getx() + 1)
        ledmatrix.set_pixel(ini.getx(),ini.gety(),ini.getfarbe()[0],ini.getfarbe()[1],ini.getfarbe()[2])
        pass

        
    elif ini.getx() is 5 and ini.gety() != 1:
        ini.sety(ini.gety() - 1)
        ledmatrix.set_pixel(ini.getx(),ini.gety(),ini.getfarbe()[0],ini.getfarbe()[1],ini.getfarbe()[2])
        pass
        
    elif ini.gety() is 1 and ini.getx() != 1:
        ini.setx(ini.getx() - 1)
        ledmatrix.set_pixel(ini.getx(),ini.gety(),ini.getfarbe()[0],ini.getfarbe()[1],ini.getfarbe()[2])
    
    else: 
        print("ups")
        
def gbl(ini):
    if ini.getshow() is False:
        ledmatrix.set_pixel(ini.getx(),ini.gety(),ini.getfarbe()[0],ini.getfarbe()[1],ini.getfarbe()[2])
        ini.setshow(True)
    else:
        ini.setshow(False)
        
    

    

# ---xy ledmatrix----
#  y 15 25 35 45 55  
#  y 14          54 
#  y 13          53  
#  y 12          52  
#  y 11 21 31 41 51  
#    xxxxxxxxxxxxxx 
    
a = Player()
b = Player()
c = Player()
d = Player()
e = Player()
f = Player()
g = Player()
h = Player()
i = Player()



a.setfarbe(255,0,0)
b.setfarbe(0,255,0)
c.setfarbe(0,0,255)
d.setfarbe(255,0,255)
e.setfarbe(255,175,0)
f.setfarbe(255, 128, 0)
g.setfarbe(255,255,255)
h.setfarbe(255,255,0)
i.setfarbe(0,150,200)

a.setx(1)
a.sety(1)

b.setx(1)
b.sety(5)

c.setx(5)
c.sety(5)

d.setx(5)
d.sety(1)

e.setx(3)
e.sety(5)

f.setx(5)
f.sety(3)

g.setx(1)
g.sety(3)

h.setx(3)
h.sety(1)

i.setx(3)
i.sety(3)


while True:
    showmap(0,0,0)

    loop(a)
    loop(b)
    loop(c)
    loop(d)
    loop(e)
    loop(f)
    loop(g)
    loop(h)
    gbl(i)
    ledmatrix.show()
    ledmatrix.clear()
    time.sleep(0.3)