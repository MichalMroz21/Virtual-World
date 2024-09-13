import random
from Zwierze import Zwierze
from zwierzeta.Wilk import Wilk
from zwierzeta.Owca import Owca
from zwierzeta.Lis import Lis
from zwierzeta.Zolw import Zolw
from zwierzeta.Antylopa import Antylopa
from zwierzeta.Czlowiek import Czlowiek
from zwierzeta.Cyberowca import Cyberowca

from rosliny.Trawa import Trawa
from rosliny.Mlecz import Mlecz
from rosliny.Guarana import Guarana
from rosliny.Jagody import Jagody
from rosliny.Barszcz import Barszcz

import math

class Swiat():
    
    def __init__(self, rozm, plansz, cred, hex):

        self.__rozmiar = rozm
        self.__obecnaTura = 0
        self.__plansza = plansz
        self.__credits = cred
        self.__Log = []
        self.__turaUmiejetnosc = -5
        self.__buttonWait = True
        self.__isSave = False
        self.__isHex = hex
        self.__prevTura = []

    def getIsHex(self):
        return self.__isHex

    def setIsHex(self, b):
        self.__isHex = b

    def getObecnaTura(self):
        return self.__obecnaTura

    def getIsSave(self):
        return self.__isSave

    def changeIsSave(self, b):
        self.__isSave = b

    def getButtonWait(self):
        return self.__buttonWait

    def changeButtonWait(self, b):
        self.__buttonWait = b

    def getTuraUmiejetnosc(self):
        return self.__turaUmiejetnosc

    def changeTuraUmiejetnosc(self, i):
        self.__turaUmiejetnosc = i

    def getObecnaTura(self):
        return self.__obecnaTura

    def getPlansza(self):
        return self.__plansza

    def changePlansza(self, planszaNew):
        self.__plansza = planszaNew

    def changeCredits(self, creditsNew):
        self.__credits = creditsNew

    def changeObecnaTura(self, i):
        self.__obecnaTura = i

    def changeRozmiarX(self, x):
        self.__rozmiar[0] = x

    def changeRozmiarY(self, y):
        self.__rozmiar[1] = y

    def getRozmiarX(self):
        return self.__rozmiar[0]

    def getRozmiarY(self):
        return self.__rozmiar[1]

 #--------------------------------------------

    def partitionOrganizm(self, i, j, organizmy):

        r = random.randrange(1, 50)

        tempL = [j, i]

        if r <= 20:
            return

        elif r <= 22:
            antylopa = Antylopa(self, tempL)
            organizmy[i].append(antylopa)

        elif r <= 24:
            cyberowca = Cyberowca(self, tempL)
            organizmy[i].append(cyberowca)

        elif r <= 26:
            lis = Lis(self, tempL)
            organizmy[i].append(lis)

        elif r <= 28:
            owca = Owca(self, tempL)
            organizmy[i].append(owca)

        elif r <= 30:
            wilk = Wilk(self, tempL)
            organizmy[i].append(wilk)

        elif r <= 32:
            zolw = Zolw(self, tempL)
            organizmy[i].append(zolw)

        elif r <= 34:
            barszcz = Barszcz(self, tempL)
            organizmy[i].append(barszcz)

        elif r <= 36:
            guarana = Guarana(self, tempL)
            organizmy[i].append(guarana)

        elif r <= 38:
            jagody = Jagody(self, tempL)
            organizmy[i].append(jagody)

        elif r <= 40:
            mlecz = Mlecz(self, tempL)
            organizmy[i].append(mlecz)

        elif r <= 42:
            trawa = Trawa(self, tempL)
            organizmy[i].append(trawa)

    #--------------------------------------------

    def rysujSwiat(self, organizmy):
        
        for i in range(0, len(self.__credits)):

            for j in range(0, len(self.__credits[i])):

                print(self.__credits[i][j], end='')

        for i in range(0, len(self.__plansza)):
            
            for j in range(0, len(self.__plansza[i])):

                print(self.__plansza[i][j], end='')

            print(' ')

        print(' ')
        print("Obecna tura: " + str(self.__obecnaTura))
        print("Nastepna tura (t)")
        print("Wyjscie (e)")
        print("Zapisz stan gry (z)")
        print("Zaladuj stan gry (l)")

        if(self.__obecnaTura != 0):

            print(' ')
            print("Organizmy z poprzedniej tury:")

            cnt = 0

            for i in range(0, len(self.__prevTura)):

                for j in range(0, len(self.__prevTura[i])):

                    print(self.__prevTura[i][j] + "   ", end='')

                    if cnt == 6: 
                        print('')
                        cnt = 0

                    else: cnt += 1

        self.__prevTura.clear()

        print(' ') 
        print(' ')
        print("Organizmy obecnie:")

        cnt = 0

        for i in range(0, len(organizmy)):

            self.__prevTura.append([])

            for j in range(0, len(organizmy[i])):

                temp = organizmy[i][j].getZnak() + ': y: ' + str(organizmy[i][j].getPolozenieI(1)) + ' x: ' + str(organizmy[i][j].getPolozenieI(0))
                print(temp + "   ", end='')
                self.__prevTura[i].append(temp)

                if cnt == 6: 
                    print('')
                    cnt = 0

                else: cnt += 1

        print(' ') 
        print(' ')

        for i in range(0, len(self.__Log)):
            print(self.__Log[i], end='')

    #--------------------------------------------

    def wykonajTure(self, organizmy):

        listOfMoves = []

        listOfMoves.append("\n")
        listOfMoves.append("Kolejnosc wykonania ruchow (wiek podczas wykonywania ruchu): ")

        self.clearLog()

        self.__obecnaTura += 1

        sortedList = []

        for i in range(0, len(organizmy)):

            for j in range(0, len(organizmy[i])):

                sortedList.append(organizmy[i][j])

        sortedList.sort(key = lambda x: (-x.getInicjatywa(), -x.getWiek() )) 

        blackList = []

        for i in range(0, len(sortedList)):

            flag = True

            for j in range(0, len(blackList)):
                if blackList[j] == i: flag = False

            if flag == False: 
                continue

            else:  
               listOfMoves.append(str(len(listOfMoves) - 1) + ". Organizm " + sortedList[i].getZnak() + " z pola y: " + str(sortedList[i].getPolozenieI(1)) + " x: " + str(sortedList[i].getPolozenieI(0)) + " inicjatywa: " + str(sortedList[i].getInicjatywa()) + " wiek: " + str(sortedList[i].getWiek()) ) 
               sortedList[i].akcja(blackList, sortedList, organizmy)
               

        for i in range(0, len(organizmy)):

            for j in range(0, len(organizmy[i])):

                organizmy[i][j].addOneToWiek()

        for i in listOfMoves:
            self.addToLog(i)

    #--------------------------------------------

    def edytujPlansze(self, x, y, c):

        if x < 0 or y < 0 or x >= self.getRozmiarX() or y >= self.getRozmiarY(): 
            return

        else: 
            self.__plansza[y][x] = c

    #--------------------------------------------

    def addToLog(self, str):

        self.__Log.append(str)
        self.__Log.append('\n')

    def clearLog(self):

        self.__Log.clear()

    def getLogOutOfEndl(self):

        ret = []

        for i in range(0, len(self.__Log)):
            if(self.__Log[i] != '\n'): ret.append(self.__Log[i])

        return ret


    def clearPrevTura(self):

        self.__prevTura.clear()

    def getLog(self):

        return self.__Log

    def getPrevTura(self):

        return self.__prevTura

    #--------------------------------------------

    def sprawdzPole(self, x, y):

        if x < 0 or y < 0 or x >= self.getRozmiarX() or y >= self.getRozmiarY(): return '\0'
        else: return self.__plansza[y][x]

    #--------------------------------------------

    def sprawdzCzyBarszczIstnieje(self):

        for y in range(0, len(self.__plansza)):
            
           for x in range(0, len(self.__plansza[y])):

               if self.sprawdzPole(x, y) == 'B': return True

        return False

    #--------------------------------------------

    def obliczDystans(self, x1, y1, x2, y2):

        return math.hypot(x2 - x1, y2 - y1)

    #--------------------------------------------

    def znajdzBarszczNajmniejszyDystans(self, xOwcy, yOwcy):

        dystanse = []

        for i in range(0, len(self.__plansza)):
            
           for j in range(0, len(self.__plansza[i])):

               if self.sprawdzPole(j, i) == 'B':

                   dystanse.append([self.obliczDystans(j, i, xOwcy, yOwcy), j, i])

        dystanseMin = min(dystanse, key = lambda l: l[0])

        return [dystanseMin[1], dystanseMin[2]]

    #--------------------------------------------

    def znajdzRuchCyberOwcy(self, xOwcy, yOwcy, xBarszcz, yBarszcz):

        polaWokol = [[xOwcy, yOwcy - 1], [xOwcy, yOwcy + 1], [xOwcy + 1, yOwcy], [xOwcy - 1, yOwcy]]

        if self.getIsHex():

            polaWokol.append([xOwcy + 1, yOwcy - 1])
            polaWokol.append([xOwcy - 1, yOwcy + 1])

        rezultat = []

        for i in polaWokol:

            if i[0] >= 0 and i[0] < self.getRozmiarX() and i[1] >= 0 and i[1] < self.getRozmiarY():

                rezultat.append([self.obliczDystans(i[0], i[1], xBarszcz, yBarszcz), i])

        rezultatMin = min(rezultat, key = lambda l: l[0])

        return [ rezultatMin[1][0], rezultatMin[1][1] ]

    #--------------------------------------------

    def makeMove(self, polozenie, teoretyczna, swiat, zasieg, kierunek, uderzajacy):

        if uderzajacy.isCyber() and self.sprawdzCzyBarszczIstnieje():

            xBarszcz, yBarszcz = self.znajdzBarszczNajmniejszyDystans(polozenie[0], polozenie[1])
            xOwcy, yOwcy = self.znajdzRuchCyberOwcy(polozenie[0], polozenie[1], xBarszcz, yBarszcz)

            teoretyczna[0] = xOwcy
            teoretyczna[1] = yOwcy

            return

        if not swiat.getIsHex():

            flags = [False, False, False, False]

            if polozenie[1] - zasieg < 0:
                flags[0] = True

            if polozenie[1] + zasieg >= self.getRozmiarY():
                flags[1] = True

            if polozenie[0] - zasieg < 0:
                flags[2] = True

            if polozenie[0] + zasieg >= self.getRozmiarX():
                flags[3] = True

            r = 0

            if kierunek == 0:

                while True:

                    r = random.randrange(0, 4)
                    if not flags[r]: break

            else:

                r = kierunek - 1

                if flags[r]:
                    teoretyczna[0] = -1
                    teoretyczna[1] = -1
                    return

            if r == 0:
                teoretyczna[1] = polozenie[1] - zasieg
                teoretyczna[0] = polozenie[0]

            if r == 1:
                teoretyczna[1] = polozenie[1] + zasieg
                teoretyczna[0] = polozenie[0]

            if r == 2:
                teoretyczna[0] = polozenie[0] - zasieg
                teoretyczna[1] = polozenie[1]

            if r == 3:
                teoretyczna[0] = polozenie[0] + zasieg
                teoretyczna[1] = polozenie[1]

        else:

            flags = [False, False, False, False, False, False]

            if polozenie[1] - zasieg < 0:
                flags[0] = False
              
            if polozenie[1] - zasieg < 0 and polozenie[0] + zasieg >= self.getRozmiarX():
                flags[1] = False

            if polozenie[1] + zasieg >= self.getRozmiarY() and polozenie[0] - zasieg < 0:
                flags[2] = False
            
            if polozenie[1] + zasieg >= self.getRozmiarY():
                flags[3] = False

            if polozenie[0] - zasieg < 0:
                flags[4] = False

            if polozenie[0] + zasieg >= self.getRozmiarX():
                flags[5] = False

            r = 0

            if kierunek == 0:

                while True:

                    r = random.randrange(0, 6)
                    if not flags[r]: break

            else:

                r = kierunek - 1

                b = False

                if r == 0:

                    b = flags[0] and flags[1]
                    r = random.randrange(0, 2)

                elif r == 1:

                    b = flags[2] and flags[3]
                    r = random.randrange(2, 4)

                elif r == 2:

                    b = flags[4]
                    r = 4

                elif r == 3:

                    b = flags[5]
                    r = 5

                if b:

                    teoretyczna[0] = -1
                    teoretyczna[1] = -1
                    return

            if r == 0:

                teoretyczna[1] = polozenie[1] - zasieg
                teoretyczna[0] = polozenie[0]

            if r == 1:

                teoretyczna[1] = polozenie[1] - zasieg
                teoretyczna[0] = polozenie[0] + zasieg

            if r == 2:

                teoretyczna[1] = polozenie[1] + zasieg
                teoretyczna[0] = polozenie[0] - zasieg

            if r == 3:

                teoretyczna[1]  = polozenie[1] + zasieg
                teoretyczna[0] = polozenie[0]

            if r == 4:

                teoretyczna[1] = polozenie[1]
                teoretyczna[0] = polozenie[0] - zasieg

            if r == 5:

                teoretyczna[1] = polozenie[1]
                teoretyczna[0] = polozenie[0] + zasieg


    #--------------------------------------------

    def changePositionOrganizm(self, x, y, newX, newY, organizmy):

        for i in range(0, len(organizmy)):

            for j in range(0, len(organizmy[i])):

                if organizmy[i][j].getPolozenieI(0) == x and organizmy[i][j].getPolozenieI(1) == y:

                    organizmy[i][j].changePolozenie(newX, newY)

    #--------------------------------------------

    def dodajPoRozmnozeniu(self, organizmy, uderzajacy, uderzony, x, y, swiat):

        s = uderzajacy.getZnak()
        swiat.edytujPlansze(x, y, s)

        swiat.addOrganizmByXY(x, y, organizmy, uderzajacy.getZnak())

        temp = "Organizm " + uderzajacy.getZnak() + " będący na y: " + str(uderzajacy.getPolozenieI(1)) + " x: " + str(uderzajacy.getPolozenieI(0)) + " rozmnożył się z " + uderzony.getZnak() + " będącym na y: " + str(uderzony.getPolozenieI(1)) + " x: " + str(uderzony.getPolozenieI(0)) + " a potomek jest na y: " + str(y) + " x: " + str(x)

        swiat.addToLog(temp)

        return False

    #--------------------------------------------

    def addOrganizmByXY(self, x, y, organizmy, c):

        tempL = [x, y]

        self.deleteOrganizmByXY(x, y, organizmy)

        if c == 'W':
            temp = Wilk(self, tempL)
            organizmy[y].append(temp)

        if c == 'O':
            temp = Owca(self, tempL)
            organizmy[y].append(temp)

        if c == 'L':
            temp = Lis(self, tempL)
            organizmy[y].append(temp)

        if c == 'Z':
            temp = Zolw(self, tempL)
            organizmy[y].append(temp)

        if c == 'A':
            temp = Antylopa(self, tempL)
            organizmy[y].append(temp)

        if c == 'T':
            temp = Trawa(self, tempL)
            organizmy[y].append(temp)

        if c == 'M':
            temp = Mlecz(self, tempL)
            organizmy[y].append(temp)

        if c == 'G':
            temp = Guarana(self, tempL)
            organizmy[y].append(temp)

        if c == 'J':
            temp = Jagody(self, tempL)
            organizmy[y].append(temp)

        if c == 'B':
            temp = Barszcz(self, tempL)
            organizmy[y].append(temp)

        if c == 'C':
            temp = Czlowiek(self, tempL)
            organizmy[y].append(temp)

        if c == 'o':
            temp = Cyberowca(self, tempL)
            organizmy[y].append(temp)

    #--------------------------------------------

    def rozmnazanie(self, organizmy, uderzajacy, uderzony):

        y1 = uderzajacy.getPolozenieI(1)
        y2 = uderzony.getPolozenieI(1)

        x1 = uderzajacy.getPolozenieI(0)
        x2 = uderzony.getPolozenieI(0)

        if y1 - 1 >= 0 and self.sprawdzPole(x1, y1 - 1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1, y1 - 1, self)

        elif y1 + 1 < self.getRozmiarY() and self.sprawdzPole(x1, y1 + 1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1, y1 + 1, self)

        elif x1 - 1 >= 0 and self.sprawdzPole(x1 - 1, y1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1 - 1, y1, self)

        elif x1 - 1 >= 0 and y1 + 1 < self.getRozmiarY() and self.sprawdzPole(x1 - 1, y1 + 1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1 - 1, y1 + 1, self)

        elif x1 - 1 >= 0 and y1 - 1 >= 0 and self.sprawdzPole(x1 - 1, y1 - 1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1 - 1, y1 - 1, self)

        elif x2 + 1 < self.getRozmiarX() and self.sprawdzPole(x2 + 1, y2) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 + 1, y2, self)

        elif x2 - 1 >= 0 and self.sprawdzPole(x2 - 1, y2) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 - 1, y2, self)

        elif x2 + 1 < self.getRozmiarX() and y2 + 1 < self.getRozmiarY() and self.sprawdzPole(x2 + 1, y2 + 1) == ' ': 
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 + 1, y2 + 1, self)
            
        elif x2 + 1 < self.getRozmiarX() and y2 - 1 >= 0 and self.sprawdzPole(x2 + 1, y2 - 1) == ' ': 
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 + 1, y2 - 1, self)
            
        elif y2 + 1 < self.getRozmiarY() and self.sprawdzPole(x2, y2 + 1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2, y2 + 1, self)
            
        elif y2 + 1 < self.getRozmiarY() and x2 + 1 < self.getRozmiarX() and self.sprawdzPole(x2 + 1, y2 + 1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 + 1, y2 + 1, self)
            
        elif y2 + 1 < self.getRozmiarY() and x2 - 1 >= 0 and self.sprawdzPole(x2 - 1, y2 + 1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 - 1, y2 + 1, self)
            
        elif y2 - 1 < self.getRozmiarY() and x2 - 1 >= 0 and self.sprawdzPole(x2 - 1, y2 - 1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 - 1, y2 - 1, self)
            
        elif y2 - 1 >= 0 and self.sprawdzPole(x2, y2 - 1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2, y2 - 1, self)
            
        elif x1 + 1 < self.getRozmiarX() and self.sprawdzPole(x1, y1) == ' ':
            self.dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1 + 1, y1, self)
            
    #--------------------------------------------

    def findOrganizmByChar(self, c, organizmy):

        for i in range(0, len(organizmy)):

            for j in range(0, len(organizmy[i])):

                if organizmy[i][j].getZnak() == c: return organizmy[i][j]
        
        return organizmy[0]

    #--------------------------------------------

    def findOrganizmByXY(self, posX, posY, organizmy):

        for i in range(0, len(organizmy)):

            for j in range(0, len(organizmy[i])):

                if organizmy[i][j].getPolozenieI(0) == posX and organizmy[i][j].getPolozenieI(1) == posY: return organizmy[i][j]

        return organizmy[0]

    #--------------------------------------------

    def deleteOrganizmByXY(self, posX, posY, organizmy):

        for i in range(0, len(organizmy)):

            for j in range(0, len(organizmy[i])):

                if organizmy[i][j].getPolozenieI(0) == posX and organizmy[i][j].getPolozenieI(1) == posY: 
                    organizmy[i].pop(j)
                    return

    #--------------------------------------------

    def zmienSileByXY(self, posX, posY, organizmy, zmiana):

        for i in range(0, len(organizmy)):

            for j in range(0, len(organizmy[i])):

                if organizmy[i][j].getPolozenieI(0) == posX and organizmy[i][j].getPolozenieI(1) == posY: 
                    
                    organizmy[i][j].zmienSile(organizmy[i][j].getSila() + zmiana)

    #--------------------------------------------

    def findAndDelete(self, x, y, organizmy, swiat, uderzajacy, temp):

        if swiat.findOrganizmByXY(x, y, organizmy) != organizmy[0]:

            if not swiat.findOrganizmByXY(x, y, organizmy).isPlant() and not swiat.findOrganizmByXY(x, y, organizmy).isCyber():

                temp.append(str(len(temp) + 1) + ". Organizm " + swiat.sprawdzPole(x, y) + " ktory byl na polu y: " + str(y) + " x: " + str(x))

                swiat.edytujPlansze(x, y, " ")
                swiat.deleteOrganizmByXY(x, y, organizmy)       

                return True
        
        return False

    #--------------------------------------------

    def usunWokol(self, x, y, organizmy, uderzajacy):

        licznik = 0

        temp = []

        if y - 1 >= 0 and self.sprawdzPole(x, y - 1) != ' ':
            if self.findAndDelete(x, y - 1, organizmy, self, uderzajacy, temp): licznik += 1

        if y - 1 >= 0 and x + 1 < self.getRozmiarX() and self.sprawdzPole(x + 1, y - 1) != ' ':
            if self.findAndDelete(x + 1, y - 1, organizmy, self, uderzajacy, temp): licznik += 1

        if y + 1 < self.getRozmiarY() and self.sprawdzPole(x, y + 1) != ' ':
            if self.findAndDelete(x, y + 1, organizmy, self, uderzajacy, temp): licznik += 1

        if x - 1 >= 0 and self.sprawdzPole(x - 1, y + 1) != ' ' and y + 1 < self.getRozmiarY(): 
            if self.findAndDelete(x - 1, y + 1, organizmy, self, uderzajacy, temp): licznik += 1

        if x - 1  >= 0 and self.sprawdzPole(x - 1, y) != ' ':
            if self.findAndDelete(x - 1, y, organizmy, self, uderzajacy, temp): licznik += 1

        if x + 1 < self.getRozmiarX() and self.sprawdzPole(x + 1, y) != ' ': 
            if self.findAndDelete(x + 1, y, organizmy, self, uderzajacy, temp): licznik += 1

        if not self.getIsHex():
            
            if x - 1 >= 0 and self.sprawdzPole(x - 1, y - 1) != ' ' and y - 1 >= 0:
                if self.findAndDelete(x - 1, y - 1, organizmy, self, uderzajacy, temp): licznik += 1

            if x + 1 < self.getRozmiarX() and self.sprawdzPole(x + 1, y + 1) != ' ' and y + 1 < self.getRozmiarY():
                if self.findAndDelete(x + 1, y + 1, organizmy, self, uderzajacy, temp): licznik += 1


        tmp = "Organizm " + uderzajacy.getZnak() + " będący na polu y: " + str(y) + " x: " + str(x) + " zabił wokól siebie " + str(licznik) + " zwierząt:"

        self.addToLog(tmp)

        for i in range(0, len(temp)):
            self.addToLog(temp[i])

    #--------------------------------------------


