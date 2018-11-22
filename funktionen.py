import random
import time
from klassen import *
from ptpulse import ledmatrix

    # -------------------------Zufallsberechnungen-----------------------------

def rndchar():
    int = random.randint(1, 5)
    return int

def atk(low, high):
    int = random.randint(low, high)
    return int

def ausweichen(prozent):
    int = random.randint(1, 100)
    if int <= prozent:
        return True
    else:
        return False

def treffen(trefferchance):
    int = random.randint(1, 100)
    if int <= trefferchance:
        return True
    else:
        return False

def kritisch(kritchance):
    int = random.randint(1, 100)
    if int <= kritchance:
        return True
    else:
        return False

def blocken(blockchance):
    int = random.randint(1, 100)
    if int <= blockchance:
        return True
    else:
        return False

def parrieren(parrychance):
    int = random.randint(1, 100)
    if int <= parrychance:
        return True
    else:
        return False

    # -------------------------Kampf Schadensberechnung---------------------------

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

    if pgy < pgx:
        pg = pgx
    elif pgx < pgy:
        pg = pgy
    else:
        pg = (pgx + pgy) / 2
    return pg

def rangecheck(p1, p2):
    dist = getDistance(p1, p2)
    hitrange = p1.getrange()
    if dist <= hitrange:
        return True
    else: 
        return False

def evade(p1, p2):
    xpos1 = p1.getx()
    ypos1 = p1.gety()
    xpos2 = p1.getx()
    ypos2 = p2.gety()
    rnd = random.randint(1, 2)
    
    xposg = xpos1 - xpos2
    yposg = ypos1 - ypos2
#   xposg positiv -> rechts
#   xposg negativ -> links
#   yposg positiv -> oben
#   yposg negativ -> unten

# ---xy ledmatrix----
#  y 06 16 26 36 46 56 66
#  y 05 15 25 35 45 55 65 
#  y 04 14 24 34 44 54 64
#  y 03 13 23 33 43 53 63  
#  y 02 12 22 32 42 52 62 
#  y 01 11 21 31 41 51 61 
#  y 00 10 20 30 40 50 60
#    xxxxxxxxxxxxxx 
#    if xposg > 0 and yposg > 0:
#    # 
#    elif xposg > 0 and yposg < 0:
#    #
#    elif xposg > 0 and yposg == 0:
#    #
#    elif xposg < 0 and yposg > 0:
#    #
#    elif xposg < 0 and yposg < 0:
#    #
#    elif xposg < 0 and yposg == 0:
#    #
#    elif xposg == 0 and yposg < 0:
#
#    elif xposg == 0 and yposg > 0:
#    #
#    elif xposg == 0 and yposg == 0:
#    #gleich
    
#   
#        if ypos1 != 3:
#            if ypos1 < 3:
#                if ypos1 < 6:
#                    ypos1 = ypos1 + 1
#            else:
#                if ypos1 > 0:
#                    ypos1 = ypos1 - 1
#        else:
#            if rnd == 1:
#                ypos1 = ypos1 + 1
#            else:
#                ypos1 = ypos1 - 1
#    
#    elif xpos1 != xpos2:
#        if ypos1 != 3:
#            if ypos1 < 3:
#                if xpos1 < 6:
#                    xpos1 = xpos1 + 1
#            else:
#                if xpos1 > 0:
#                    xpos1 = xpos1 - 1
#        else:
#            if rnd == 1:
#                xpos1 = xpos1 + 1
#            else:
#                xpos1 = xpos1 - 1

#    p1.setx(xpos1)
#    p1.sety(ypos1)

def jagt(jaeger, gejagter):
    jx = jaeger.getx()
    jy = jaeger.gety()
    gx = gejagter.getx()
    gy = gejagter.gety()

    if jx < gx:
        jaeger.setx(jx + 1)
    
    if jx > gx:
        jaeger.setx(jx - 1)
    
    if jy < gy:
        jaeger.sety(jy + 1)
        
    if jy > gy:
        jaeger.sety(jy - 1)
    
def angriff(frame, angreifer, verteidiger):
    angreiferatk = atk(angreifer.getatklow(), angreifer.getatkhigh())
    angreiferhit = treffen(angreifer.gethit())
    angreifercrit = kritisch(angreifer.getcrit())
    verteidigerdodge = ausweichen(verteidiger.getdodge())
    verteidigerblock = blocken(verteidiger.getblock())
    verteidigerparry = parrieren(verteidiger.getparry())
    verteidigerhpget = verteidiger.gethp()
    angreifername = angreifer.getname()
    verteidigername = verteidiger.getname()
    
    print(frame.counter, angreifer.atkvar)
    
    if rangecheck(angreifer, verteidiger) == True:
        dmg = 0
        if angreiferhit == True:
            if verteidigerdodge == False:
                if verteidigerparry == False:
                    if verteidigerblock == True:
                        if angreifer.getmeele() == False:
                            dmg = angreiferatk / 2
                            status = 1
                            rangeattackspawn(frame, angreifer, verteidiger, dmg, status)
                        else:
                            print(angreifername, "'s Angriff wurde geblockt und macht", angreiferatk / 2, "Schaden")
                            hurt(verteidiger, 1)
                            dmg = angreiferatk / 2
                            verteidiger.sethp(verteidigerhpget - dmg)
                    else:
                        if angreifercrit == True:
                            if angreifer.getmeele() == False:
                                dmg = angreiferatk * 2
                                status = 3
                                rangeattackspawn(frame, angreifer, verteidiger, dmg, status)
                            else:
                                dmg = angreiferatk * 2
                                verteidiger.sethp(verteidigerhpget - dmg)
                                print("BAM! ", angreifername, "Krittet fuer", angreiferatk * 2, "Schaden!")
                                hurt(verteidiger, 3)
                        else:
                            if angreifer.getmeele() == False:
                                dmg = angreiferatk
                                status = 2
                                rangeattackspawn(frame, angreifer, verteidiger, dmg, status)
                            else:
                                dmg = angreiferatk
                                verteidiger.sethp(verteidigerhpget - dmg)
                                print(angreifername, "macht", angreiferatk, "Schaden.")
                                hurt(verteidiger, 2)
                else:
                    print(verteidigername, "hat pariert")
            else:
                #evade(verteidiger, angreifer)
                print(verteidigername, "ist ausgewichen!")
        else:
            print(angreifername, "hat verfehlt!")
        
    else:
        # print("Zu weit entfernt")
        dmg = 0

    
#    print(angreifer.getname(), "HP:", angreifer.gethp(), "/", angreifer.gethpmax(), "  ", verteidiger.getname(), "HP:", verteidiger.gethp(), "/", verteidiger.gethpmax())

def rangeattackspawn(frame, p1, p2, dmg, status):
    pew = Shot()
    frame.actcl.append(pew)
    sc = frame.shotcounter
    sc = sc + 1
    frame.setshotcounter(sc)
    pew.setshotid(sc)
    pew.setdamage(dmg)
    pew.setstatus(status)
    pew.settarget(p2)
    pew.setcaster(p1)
    pew.setx(p1.getx())
    pew.sety(p1.gety())
    jagt(pew, p2)

def shotchase(frame, player):
    dist = rangecheck(player, player.target)
    
    if dist == True:
        player.target.sethp(player.target.hpvar - player.damage)
        print(player.caster.name,"'s Schuss macht", player.damage, "Schaden.")
        status = player.getstatus()
        player.setshow(False)
        hurt(player.target, status)
        player.setdamage(0)
        player.setkill(True)
        
    else:
        jagt(player, player.target)
    

    # -----------------------------Charakter Wahl-------------------------------

def charwahl(i):
    if i == 1:
        char = Krieger()
    elif i == 2:
        char = Schurke()
    elif i == 3:
        char = Riese()
    elif i == 4:
        char = Magier()
    elif i == 5:
        char = Bogenschuetze()
    return char

# ----------------------------------Charakter steuerung -------------------------------------

def playeroption(frame, player):
    if player.shotid >= 1:
        shotchase(frame, player)
    else:
        if player.attack is True and rangecheck(player, player.target) is True:
            angriff(frame, player, player.target)
            player.attack = False
        elif player.movement is True and rangecheck(player, player.target) is False:
            jagt(player, player.target)
            player.movement = False
        else:
            pass

# ----------------------------------Runden steuerung-----------------------------------------

def tick(frame):
    counter = frame.getcounter()
    counter = counter + 1 
    frame.setcounter(counter)
    
    for i in frame.actcl:
        i.settick(True)
    time.sleep(0.1)

# ----------------------------------Start----------------------------------------------------

def start():
    frame = Frame()
    ac = frame.actcl
    a = charwahl(rndchar()) #(playerchar)
    b = charwahl(rndchar())
    ac = [a, b]
    a.settarget(b)
    b.settarget(a)
    frame.setactcl(ac)
    reset(ac)
    startintro(a, b)
    initialisierung(frame)
    return frame

# -----------------------------------Lebenserhaltung-----------------------------------------

def lifecheck(frame):
    counter = 0
    if frame.actcl[0].alive is True:
            counter = counter + 1
    if frame.actcl[1].alive is True:
            counter = counter + 1
    return counter

# ----------------------------------Initialisierung------------------------------------------

def initialisierung(frame):
    ac = frame.actcl
    pn = lifecheck(frame)
    # runden basierung startet hier
    while pn > 1:
        starttime = time.time()
        tick(frame)
        for i in range(0, len(ac)):
            activechar = frame.actcl[i]
            playeroption(frame, activechar)
            display(frame)
        clearkill(frame)
        pn = lifecheck(frame)
        endtime = time.time()
        #print(endtime - starttime)

    if pn == 1:
        if frame.actcl[0].alive == True:
            print(frame.actcl[0].getname(), "gewinnt!")
            showdeath(0)
            ledmatrix.show()
        
        elif frame.actcl[1].alive == True:
            print(ac[1].getname(), "gewinnt!")
            showdeath(6)
            ledmatrix.show()
    
    else:
        print("Beide sind tot!")
        showloose()
        ledmatrix.show()

def reset(ac):
    a = ac[0]
    b = ac[1]
    a.setx(0)
    a.sety(3)
    b.setx(6)
    b.sety(3)

def clearkill(frame):
    ac = frame.actcl
    num = len(ac)
    for i in range(0, len(ac)):
        killcheck = ac[i].kill
        if killcheck == True:
            frame.actcl.pop(i)
            num = num - 1
            break

# -----------------------------------LED BAR--------------------------------------------------

# ---xy ledmatrix----
#  y 06 16 26 36 46 56 66
#  y 05 15 25 35 45 55 65 
#  y 04 14 24 34 44 54 64
#  y 03 13 23 33 43 53 63  
#  y 02 12 22 32 42 52 62 
#  y 01 11 21 31 41 51 61 
#  y 00 10 20 30 40 50 60
#    xxxxxxxxxxxxxx 

def display(frame):
    ledmatrix.rotation(0)
    ledmatrix.clear()
    showmap(80, 80, 80)
    ac = frame.actcl
    hpbar(ac[0], ac[1])
    for i in range(0,len(ac)):
        showvar = ac[i].getshow()
        if showvar is True:
            showplayer(ac[i])
    ledmatrix.show()
    
def showmap(r, g, b):
    for x in range(0, 7):
        for y in range(1, 6):
            rr = int(r)
            gg = int(g)
            bb = int(b)
            ledmatrix.set_pixel(x, y, rr, gg, bb)

def showdeath(ini):
    for x in range(0 ,7):
        ledmatrix.set_pixel(x, ini, 255, 0, 0)    
    
def showloose():
    for x in range(0 ,7):
        ledmatrix.set_pixel(x, 6, 255, 0, 0)
    for x in range(0 ,7):
        ledmatrix.set_pixel(x, 0, 255, 0, 0)

def showplayer(ini):
    ledmatrix.set_pixel(ini.getx(),ini.gety(),ini.getfarbe()[0],ini.getfarbe()[1],ini.getfarbe()[2])

def hpbar(p1, p2):
    # top = ((0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6))
    # bot = ((0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0))
    hpmax1 = p1.gethpmax()
    hpvar1 = p1.gethp()
    hpmax2 = p2.gethpmax()
    hpvar2 = p2.gethp()
    anz1 = int(hpvar1 / hpmax1 * 100 // 14)
    anz2 = int(hpvar2 / hpmax2 * 100 // 14)
    
    if anz1 == 0:
        ledmatrix.set_pixel(0, 6, 255, 0, 0)
    for x in range(0 ,anz1):
        ledmatrix.set_pixel(x, 6, p1.getfarbe()[0], p1.getfarbe()[1], p1.getfarbe()[2])
    if anz2 == 0:
        ledmatrix.set_pixel(0, 0, 255, 0, 0)
    for x in range(0, anz2):
        ledmatrix.set_pixel(x, 0, p2.getfarbe()[0], p2.getfarbe()[1], p2.getfarbe()[2])

def startintro(player1, player2):
    ledmatrix.rotation(0)
    ledmatrix.clear()
    showmap(80, 80, 80)
    for x in range(6, -1, -1):
        ledmatrix.set_pixel(x, 6, player1.getfarbe()[0], player1.getfarbe()[1], player1.getfarbe()[2])
        ledmatrix.show()
        time.sleep(0.1)
    for x in range(0, 7, 1):
        ledmatrix.set_pixel(x, 0, player2.getfarbe()[0], player2.getfarbe()[1], player2.getfarbe()[2])
        ledmatrix.show()
        time.sleep(0.1)

    ledmatrix.set_pixel(0, 5, player1.getfarbe()[0], player1.getfarbe()[1], player1.getfarbe()[2])
    ledmatrix.set_pixel(6, 1, player2.getfarbe()[0], player2.getfarbe()[1], player2.getfarbe()[2])
    ledmatrix.show()
    time.sleep(0.1)
    ledmatrix.set_pixel(0, 4, player1.getfarbe()[0], player1.getfarbe()[1], player1.getfarbe()[2])
    ledmatrix.set_pixel(6, 2, player2.getfarbe()[0], player2.getfarbe()[1], player2.getfarbe()[2])
    ledmatrix.show()
    time.sleep(0.1)

    ledmatrix.set_pixel(0, 3, player1.getfarbe()[0], player1.getfarbe()[1], player1.getfarbe()[2])
    ledmatrix.set_pixel(6, 3, player2.getfarbe()[0], player2.getfarbe()[1], player2.getfarbe()[2])
    ledmatrix.show()
    time.sleep(0.1)

    ledmatrix.set_pixel(0, 5, 80, 80, 80)
    ledmatrix.set_pixel(6, 1, 80, 80, 80)
    ledmatrix.show()
    time.sleep(0.1)
    ledmatrix.set_pixel(0, 4, 80, 80, 80)
    ledmatrix.set_pixel(6, 2, 80, 80, 80)
    ledmatrix.show()
    time.sleep(0.1)
    
def hurt(ini, x):
    for i in range(0, x):
        ledmatrix.set_pixel(ini.getx(),ini.gety(),255, 0, 0)
        ledmatrix.show()
        time.sleep(0.05)
        ledmatrix.set_pixel(ini.getx(),ini.gety(), ini.getfarbe()[0], ini.getfarbe()[1], ini.getfarbe()[2])
        ledmatrix.show()
        time.sleep(0.05)
        