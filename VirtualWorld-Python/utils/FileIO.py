from zwierzeta.Czlowiek import Czlowiek
from zwierzeta.Antylopa import Antylopa
from zwierzeta.Cyberowca import Cyberowca
from zwierzeta.Lis import Lis
from zwierzeta.Owca import Owca
from zwierzeta.Wilk import Wilk
from zwierzeta.Zolw import Zolw

from rosliny.Barszcz import Barszcz
from rosliny.Guarana import Guarana
from rosliny.Jagody import Jagody
from rosliny.Mlecz import Mlecz
from rosliny.Trawa import Trawa


class FileIO():
    

    def makeSave(self, x, y, organizmy, turaUmiejetnosc, czyCzlowiekIstnieje, czyJestTarczaAldura, kierunekRuchu, obecnaTura, log, prevTura):

        file = open(r"save/save.txt", "w")

        czyCzlowiekIstniejeInt = 1 if czyCzlowiekIstnieje[0] else 0
        czyJestTarczaAldura = 1 if czyJestTarczaAldura else 0

        file.write("x " + str(x) + '\n')
        file.write("y " + str(y) + '\n')
        file.write("t " + str(obecnaTura) + '\n')
        file.write("c " + str(turaUmiejetnosc) + " " + str(kierunekRuchu) + " " + str(czyJestTarczaAldura) + " " + str(czyCzlowiekIstniejeInt) + '\n')

        for i in range(0, len(organizmy)):

            for j in range(0, len(organizmy[i])):

                temp = organizmy[i][j]

                file.write("o " + temp.getZnak() + " " + str(temp.getPolozenieI(0)) + " " + str(temp.getPolozenieI(1)) + " " + str(temp.getSila()) + " " + str(temp.getInicjatywa()) + " " + str(temp.getWiek()) + '\n')

        for i in range(0, len(prevTura)):

            for j in range(0, len(prevTura[i])):

                file.write("p " + prevTura[i][j] + '\n')

        for i in range(0, len(log)):

            file.write(log[i])

        file.close()

    #--------------------------------------------

    def readSave(self, swiat, organizmy):

        CREDITS_HEIGHT = 3

        file = open(r"save/save.txt", "r")

        strs = file.readlines()

        swiat.clearLog()

        swiat.clearPrevTura()

        newStrs = []

        for line in strs:

            newStrs.append(line.strip())


        ret = []

        x = 0
        y = 0

        gotX = False
        gotY = False
        alreadySet = False

        planszNew = []
        creditsNew = []
        organizmyNew = []

        nLines = []

        nLine = 0


        for line in newStrs:

            if len(line) <= 0: continue

            nLine += 1

            if gotX and gotY and alreadySet == False:

                for i in range(0, y):
                    organizmyNew.append([])

                for i in range(0, y):
                    str = "".join(' ' for i in range(x))
                    str = list(str)

                    planszNew.append(str)

                for i in range(0, CREDITS_HEIGHT):

                    if not (i % 2 > 0):

                        str = "".join('-' for i in range(x + 1))
                        str = str + '\n'
        
                        creditsNew.append(str)

                    else:

                        temp = "s188708 Michal Mroz \n"
                        creditsNew.append(temp)



                for i in range(0, swiat.getRozmiarY()):

                    swiat.getPlansza().append([])

                    for j in range(0, swiat.getRozmiarX()):

                        swiat.getPlansza()[i].append(" ")


                alreadySet = True

            
            ch = line[0]

            if ch == 'x':

                x = int(line[2:])
                ret.append(x)
                swiat.changeRozmiarX(x)
                gotX = True

            elif ch == 'y':

                y = int(line[2:])
                ret.append(y)
                swiat.changeRozmiarY(y)
                gotY = True

            elif ch == 't':

                t = int(line[2:])
                swiat.changeObecnaTura(t)

            elif ch == 'c':

                fromIndex = 0

                while line.find(' ', line.find(' ', fromIndex) + 1) != -1:

                    v = int(line[line.find(' ', fromIndex) + 1 : line.find(' ', line.find(' ', fromIndex) + 1)])

                    ret.append(v)

                    fromIndex = line.find(' ', fromIndex) + 1
                
                ret.append(int(line[line.find(' ', fromIndex) + 1 : ]))

            elif ch == 'o':
        
                fi = 2

                values = []

                while line.find(' ', line.find(' ', fi) + 1) != -1:

                    v = int(line[line.find(' ', fi) + 1 : line.find(' ', line.find(' ', fi) + 1)])

                    values.append(v)
                    
                    fi = line.find(' ', fi) + 1

                values.append(int(line[line.find(' ', fi) + 1 : ]))

                tempL = [values[0], values[1]]

                ch2 = line[2]

                temp = Antylopa(swiat, tempL)

                if ch2 == 'A':

                    temp = Antylopa(swiat, tempL)

                elif ch2 == 'B':

                    temp = Barszcz(swiat, tempL)

                elif ch2 == 'C':

                    temp = Czlowiek(swiat, tempL)

                elif ch2 == 'G':

                    temp = Guarana(swiat, tempL)

                elif ch2 == 'J':

                    temp = Jagody(swiat, tempL)

                elif ch2 == 'L':

                    temp = Lis(swiat, tempL)

                elif ch2 == 'M':

                    temp = Mlecz(swiat, tempL)

                elif ch2 == 'O':

                    temp = Owca(swiat, tempL)
                    
                elif ch2 == 'T':

                    temp = Trawa(swiat, tempL)

                elif ch2 == 'W':

                    temp = Wilk(swiat, tempL)

                elif ch2 == 'Z':

                    temp = Zolw(swiat, tempL)

                elif ch2 == 'o':

                    temp = Cyberowca(swiat, tempL)

                temp.changeWiek(values[4])
                temp.changeInicjatywa(values[3])
                temp.zmienSile(values[2])

                planszNew[values[1]][values[0]] = ch2
                organizmyNew[values[1]].append(temp)

            else:
                nLines.append(nLine)


        swiat.changePlansza(planszNew)

        swiat.changeCredits(creditsNew)

        organizmy.clear()

        for i in range(0, len(organizmyNew)):

            organizmy.append([])

        for i in range(0, len(organizmyNew)):

            for j in range(0, len(organizmyNew[i])):

                organizmy[i].append(organizmyNew[i][j])

        i = 0

        j = 0

        nLine = 0

        for n in range(0, len(organizmyNew)):

            swiat.getPrevTura().append([])

        for line in newStrs:

            if len(line) <= 0: continue

            nLine += 1

            if line[0] == 'p':

                temp = line[2:]
                swiat.getPrevTura()[i].append(temp)

                if j + 1 == len(organizmyNew[i]):

                    j = 0
                    i += 1

                else: 

                    j += 1

            elif nLine in nLines:

                temp = line
                if (temp == "Kolejność wykonania ruchów (wiek podczas wykonywania ruchu):"): swiat.addToLog("\n")
                swiat.addToLog(temp)
                

        file.close()

        return ret

        

