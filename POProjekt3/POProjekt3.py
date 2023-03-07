from Swiat import Swiat
from zwierzeta.Wilk import Wilk
from zwierzeta.Czlowiek import Czlowiek

from utils.FileIO import FileIO
from utils.Gui import Gui

import os
import time
import readchar

import pygame

from msvcrt import getch

SPACE_BETWEEN_ROUND_BOARDS = 5

CREDITS_HEIGHT = 3

fileio = FileIO()

x = 0
y = 0

isHex = False

gui = Gui()

values = gui.startDialogue()

print(values)

x = values[1]
y = values[2]

isHex = True if values[0] == 1 else False
 
credits = []

for i in range(0, CREDITS_HEIGHT):
    if not (i % 2 > 0):
        str = "".join('-' for i in range(x + 1))
        str = str + '\n'
        
        credits.append(str)

    else:
        str = "s188708 Michal Mroz\n"
        credits.append(str)

rozm = [x, y]

plansza = []

for i in range(0, y):
    str = "".join(' ' for i in range(x))
    str = list(str)

    plansza.append(str)


swiat = Swiat(rozm, plansza, credits, isHex)


organizmy = []

for i in range(0, y):
    organizmy.append([])

    
cPosY = round(y/2)
cPosX = round(x/2)

for i in range(0, y):

    for j in range(0, x):

        if i == cPosY and j == cPosX:
            temp = [j, i]
            czlowiek = Czlowiek(swiat, temp)
            organizmy[i].append(czlowiek)
            continue

        swiat.partitionOrganizm(i, j, organizmy)
            

flag = [True]

while(flag[0]):

    clear = "\n" * SPACE_BETWEEN_ROUND_BOARDS
    print(clear)

    swiat.rysujSwiat(organizmy)

    czyCzlowiekIstnieje = [False]

    if swiat.getObecnaTura() != 0: print('')

    if swiat.findOrganizmByChar('C', organizmy) != organizmy[0]:

        swiat.findOrganizmByChar('C', organizmy).podajKierunekRuchu()
        print(swiat.findOrganizmByChar('C', organizmy).podajInfoTarcza(swiat.getTuraUmiejetnosc()))
        czyCzlowiekIstnieje[0] = True

    else:

        print("Czlowiek nie zyje!")
        czyCzlowiekIstnieje[0] = False


    ch = gui.setUpGui(flag, czyCzlowiekIstnieje, swiat, organizmy, swiat.getPlansza())

    if ch == 'T':

        if czyCzlowiekIstnieje[0]:

            if swiat.findOrganizmByChar('C', organizmy).getKierunekRuchu() == 0:
                print(" Podaj strzalkami kierunek ruchu czlowieka przed rozpoczeciem tury!")
                time.sleep(1)

            else:
                swiat.wykonajTure(organizmy)

                if swiat.getTuraUmiejetnosc() != -5: swiat.changeTuraUmiejetnosc(swiat.getTuraUmiejetnosc() - 1)

                if czyCzlowiekIstnieje[0] and swiat.getTuraUmiejetnosc() == 0 and swiat.findOrganizmByChar('C', organizmy) != organizmy[0]:
                    
                    swiat.findOrganizmByChar('C', organizmy).zmienStanTarczyAldura(0)

        else:

            swiat.wykonajTure(organizmy)

            if swiat.getTuraUmiejetnosc() != 5: swiat.changeTuraUmiejetnosc(swiat.getTuraUmiejetnosc() - 1) 

            if czyCzlowiekIstnieje[0] and swiat.getTuraUmiejetnosc() == 0:
                swiat.findOrganizmByChar('C', organizmy).zmienStanTarczyAldura(0)


    if ch == 'E':
        flag[0] = False

    if ch == "UP":
        if czyCzlowiekIstnieje[0]:
            swiat.findOrganizmByChar('C', organizmy).zmienKierunekRuchu(1)

    if ch == "DOWN":
        if czyCzlowiekIstnieje[0]:
            swiat.findOrganizmByChar('C', organizmy).zmienKierunekRuchu(2)

    if ch == "LEFT":
        if czyCzlowiekIstnieje[0]:
            swiat.findOrganizmByChar('C', organizmy).zmienKierunekRuchu(3)

    if ch == "RIGHT":
        if czyCzlowiekIstnieje[0]:
            swiat.findOrganizmByChar('C', organizmy).zmienKierunekRuchu(4)

    if ch == 'U':
        if czyCzlowiekIstnieje[0] and swiat.getTuraUmiejetnosc() == -5:
            swiat.findOrganizmByChar('C', organizmy).zmienStanTarczyAldura(1)
            swiat.changeTuraUmiejetnosc(5)

        elif czyCzlowiekIstnieje[0]:
            print(" Umiejetnosc ma cooldown lub jest juz aktywowana!")
            time.sleep(0.5)

    if ch == 'Z':

        tarcza = False
        kierunekRuchu = 0

        if czyCzlowiekIstnieje[0] and swiat.findOrganizmByChar('C', organizmy) != organizmy[0]:
            tarcza = swiat.findOrganizmByChar('C', organizmy).czyJestTarczaAldura()
            kierunekRuchu = swiat.findOrganizmByChar('C', organizmy).getKierunekRuchu()


        fileio.makeSave(swiat.getRozmiarX(), swiat.getRozmiarY(), organizmy, swiat.getTuraUmiejetnosc(), czyCzlowiekIstnieje, tarcza, kierunekRuchu, swiat.getObecnaTura(), swiat.getLog(), swiat.getPrevTura())

    if ch == 'L':

        temp = fileio.readSave(swiat, organizmy)

        if temp != None:

            x = temp[0]
            y = temp[1]

            swiat.changeTuraUmiejetnosc(temp[2])

            if swiat.findOrganizmByChar('C', organizmy) != organizmy[0]:
                temp2 = swiat.findOrganizmByChar('C', organizmy)
                temp2.zmienKierunekRuchu(temp[3])
                temp2.zmienStanTarczyAldura(True if temp[4] == 1 else False)

            czyCzlowiekIstnieje[0] = True if temp[5] == 1 else False


pygame.quit()      