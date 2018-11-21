# -----------------------Bogenschuetze------------------------
class Bogenschuetze():
    def __init__(self):
        self.id =       0               # set, get 
        self.shotid = 0
        self.target = 0
        self.alive =    True
        self.kill =     False
        self.active =   False
        self.name =     "Bogenschuetze"
        self.hpmax =    25
        self.hpvar =    self.hpmax
        self.dodge =    20
        self.hit =      90
        self.atklow =   6
        self.atkhigh =  9
        self.crit =     15
        self.block =    0
        self.parry =    0
        self.x =        0
        self.y =        0
        self.farbe =    0, 255, 0  # gruen
        self.show =     True
        self.range =    6
        self.meele =    False
        self.movement = False
        self.movereq =  10
        self.movevar =  0
        self.attack =   False
        self.atkreq =   18
        self.atkvar =   0
        self.tick =     False


    def getactive(self):
        return self.active
    
    def setactive(self, wert):
        self.active = wert

    def getid(self):
        return self.id
    
    def setid(self, wert):
        self.id = wert

    def gettarget(self):
        return self.target
    
    def settarget(self, wert):
        self.target = wert

    def getalive(self):
        return self.alive
    
    def getname(self):
        return self.name

    def gethp(self):
        return self.hpvar

    def gethpmax(self):
        return self.hpmax

    def sethp(self, wert):
        self.hpvar = wert
        if self.hpvar <= 0:
            self.alive = False

    def getattack(self):
        return self.attack

    def setatkvar(self, wert):
        if self.atkvar <= self.atkreq and self.attack == False:
            self.atkvar = self.atkvar + wert
            if self.atkvar >= self.atkreq:
                self.atkvar = 0
                self.attack = True

    def setmovevar(self, wert):
        if self.movevar <= self.movereq:
            self.movevar = self.movevar + wert
            if self.movevar >= self.movereq:
                self.movevar = 0
                self.movement = True

    def resetatkvar(self):
        self.movevar = 0

    def settick(self, wert):
        self.tick = wert
        if self.tick is True:
            self.setmovevar(1)
            self.setatkvar(1)
            self.tick = False

    def getdodge(self):
        return self.dodge

    def gethit(self):
        return self.hit

    def getatklow(self):
        return self.atklow

    def getatkhigh(self):
        return self.atkhigh

    def getcrit(self):
        return self.crit

    def getblock(self):
        return self.block

    def getparry(self):
        return self.parry

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
    
    def setfarbe(self, r, g, b):
        self.farbe = r, g, b
    
    def getshow(self):
        return self.show

    def setshow(self, wert):
        self.show = wert

    def getrange(self):
        return self.range

    def getmeele(self):
        return self.meele