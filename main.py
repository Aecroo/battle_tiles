#!/usr/bin/env python3

from klassen import *
from funktionen import *
import time

done = False

while done == False:
    print("Neues Spiel!")
    newgame = "" #input("Press Enter to continue")
    if newgame == "":
        #print("waehle deinen Char")
        #playerchar = int(input("1. Krieger \n2. Schurke \n3. Riese \n4. Magier \n5. Bogenschuetze\n"))
        start()
        time.sleep(3)
    else:
        done = True

# eof