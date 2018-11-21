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
    
    def setfarbe(self,r,g,b):
        self.farbe = r,g,b

def rndplayer(ini):
    rx = random.randint(0,6)
    ry = random.randint(0,6)
    ini.setx(rx)
    ini.sety(ry)

def showmap(r, g, b):
    for x in range(0, 7):
        for y in range(0, 7):
            rr = int(r)
            gg = int(g)
            bb = int(b)
            ledmatrix.set_pixel(x, y, rr, gg, bb)

def setplayer(ini):
    ledmatrix.set_pixel(ini.getx(),ini.gety(),ini.getfarbe()[0],ini.getfarbe()[1],ini.getfarbe()[2])

def randomwalk(ini):
    seq = ["n","o","s","w"]
    daway = random.choice(seq)
    # print("daway is:",daway)
    if daway is "n":
        if ini.gety() is 6:
            ini.sety(6)
        
        else: ini.sety(ini.gety()+1)
        print("n")
    elif daway is "o":
        if ini.getx() is 6:
            ini.setx(6)
        else: ini.setx(ini.getx()+1)
        print("o")
    elif daway is "s":
        if ini.gety() is 0:
            ini.sety(0)
        else: ini.sety(ini.gety()-1)
        print("s")
    else: #daway is w:
        if ini.getx() is 0:
            ini.setx(0)
        else: ini.setx(ini.getx()-1)
        print("w")
    

def jagt(jaeger, gejagter):
    jx = jaeger.getx()
    jy = jaeger.gety()
    gx = gejagter.getx()
    gy = gejagter.gety()
    
    if jx < gx:
        jaeger.setx(jx + 1)
    
    elif jx > gx:
        jaeger.setx(jx - 1)
    
    elif jy < gy:
        jaeger.sety(jy + 1)
        
    elif jy > gy:
        jaeger.sety(jy - 1)
    
    else:
        print("nomnomnom")

def killcheck(p1, p2):
    dist = getDistance(p1, p2)
    if dist == 0:
        print("Schaf gefressen")
        return True
    else: pass

def getDistance(p1, p2):
    p1x = p1.getx()
    p1y = p1.gety()
    p2x = p2.getx()
    p2y = p2.gety()
    
    if p1x >= p2x:
        pgx = p1x - p2x
    else:
        pgx = p2x - p1x
        
    if p1y >= p2y:
        pgy = p1y - p2y
    else:
        pgy = p2y - p1y
        
    pg = pgy + pgx
    print(pg)
    return pg

def flucht(gejagter,jaeger):
    jx = jaeger.getx()
    jy = jaeger.gety()
    gx = gejagter.getx()
    gy = gejagter.gety()
    
    if jx > gx and gx != 6:
        gejagter.setx(gx - 1)
    
    elif jx < gx and gx != 0:
        gejagter.setx(gx + 1)
    
    elif jy > gy and gy != 6:
        gejagter.sety(gy - 1)
        
    elif jy < gy and gy != 0:
        gejagter.sety(gy + 1)
    
    else:
        print("blablabla")    
    
schaf = Player()
wolf = Player()
#wolf2 = Player()

wolf.setfarbe(255,0,0)
#wolf2.setfarbe(255,150,0)
schaf.setfarbe(0,0,255)

wolf.setx(0)
wolf.sety(0)
#wolf2.setx(6)
#wolf2.sety(0)

schaf.setx(4)
schaf.sety(6)

while True:
    showmap(0,200,0)
    randomwalk(schaf)
    # flucht(schaf, wolf)
    jagt(wolf, schaf)
#    jagt(wolf2, schaf)
    killw1 = killcheck(wolf, schaf)
#    killw2 = killcheck(wolf2, schaf)
    if killw1 is True:
        rndplayer(schaf)
    else:
        setplayer(schaf)
    
    setplayer(wolf)
#    setplayer(wolf2)
    
    ledmatrix.show()
    time.sleep(2)