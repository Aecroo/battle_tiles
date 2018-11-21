from krieger import *
from magier import *
from schurke import *
from riese import *
from bogenschuetze import *

class Frame():
    def __init__(self):
        self.counter = 0
        self.actcl = []
        self.shotcounter = 0

    def getcounter(self):
        return self.counter

    def setcounter(self, wert):
        self.counter = wert
    
    def getactcl(self):
        return self.actcl
    
    def setactcl(self, wert):
        self.actcl = wert

    def getshotcounter(self):
        return self.actcl
    
    def setshotcounter(self, wert):
        self.shotcounter = wert

class Shot():
    def __init__(self):
        self.shotid = 0
        self.alive = False
        self.attack =   False
        self.tick = False
        self.x = 0
        self.y = 0
        self.show = True
        self.farbe = 255, 255, 255
        self.movement = False
        self.movereq =  1
        self.movevar =  0
        self.damage = 0
        self.caster = 0
        self.target = 0
        self.range = 1
        self.kill = False
        self.status = 0
        
    def getshotid(self):
        return self.shotid
    
    def setshotid(self, wert):
        self.shotid = wert

    def setmovevar(self, wert):
        self.movevar = self.movevar + wert
        if self.movevar >= self.movereq:
            self.movement = True
            self.movevar = 0

    def settick(self, wert):
        self.tick = wert
        if self.tick is True:
            self.setmovevar(1)
            self.tick = False

    def getframebew(self):
        return self.rndtime

    def setframebew(self, wert):
        self.framebew = wert

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
    
    def getshow(self):
        return self.show
        
    def setshow(self, wert):
        self.show = wert
    
    def getdamage(self):
        return self.damage
        
    def setdamage(self, wert):
        self.damage = wert
    
    def gettarget(self):
        return self.target

    def settarget(self, wert):
        self.target = wert

    def getcaster(self):
        return self.caster

    def setcaster(self, wert):
        self.caster = wert
    
    def getrange(self):
        return self.range
    
    def getkill(self):
        return self.kill
    
    def setkill(self, wert):
        self.kill = wert
    
    def getstatus(self):
        return self.status
    
    def setstatus(self, wert):
        self.status = wert