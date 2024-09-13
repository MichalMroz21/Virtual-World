from Organizm import Organizm

class Zwierze(Organizm):
    
    def __init__(self):
        super(Organizm, self).__init__()

    def __init__(self, org):
        super(Organizm, self).__init__()

    #--------------------------------------------

    def rysowanie(self):
        print('Z')

    def getZnak(self):
        print('Z')

    def czyOdbito(self, atakujacy, blacklistAtakowany):
        return False

    def zmienPolozenie(self, swiat):
        return True

    def isPlant(self):
        return False

    def zasieg(self):
        return 1

    def ucieczka(self, teoretyczna, organizmy, blacklistAtakowany):
        return False

    def odstraszenieZPola(self, poleAtakujacego, poleAtakowanego, organizmy, odstraszonego):
        pass

    def getKierunekRuchu(self):
        return 0

    def zmienKierunekRuchu(self, a):
        pass

    def podajInfoTarcza(self, tura):
        return None

    def zmienStanTarczyAldura(self, b):
        pass

    def podajKierunekRuchu(self):
        return None

    def czyJestTarczaAldura(self):
        return False

    def isCyber(self):
        return False

    #--------------------------------------------

    def akcja(self, blackList, sortedList, organizmy):
        
        uderzajacy = self

        if uderzajacy.zmienPolozenie(self.getSwiat()):

            teoretyczna = [0, 0]

            self.getSwiat().makeMove(uderzajacy.getPolozenie(), teoretyczna, self.getSwiat(), uderzajacy.zasieg(), uderzajacy.getKierunekRuchu(), uderzajacy)

            if teoretyczna[0] == -1 and teoretyczna[1] == -1: return

            if self.getSwiat().sprawdzPole(teoretyczna[0], teoretyczna[1]) == ' ':

                xPrev = uderzajacy.getPolozenieI(0)
                yPrev = uderzajacy.getPolozenieI(1)

                self.getSwiat().edytujPlansze(uderzajacy.getPolozenieI(0), uderzajacy.getPolozenieI(1), " ")

                s = self.getZnak()

                self.getSwiat().edytujPlansze(teoretyczna[0], teoretyczna[1], s)

                self.getSwiat().changePositionOrganizm(uderzajacy.getPolozenieI(0), uderzajacy.getPolozenieI(1), teoretyczna[0], teoretyczna[1], organizmy)

                temp = "Organizm " + uderzajacy.getZnak() + " poruszył się z pola y: " + str(yPrev) + " x: " + str(xPrev) + " na wolne pole y: " + str(teoretyczna[1]) + " x: " + str(teoretyczna[0])

                self.getSwiat().addToLog(temp)

                for j in range(0, len(sortedList)):

                    if sortedList[j].getPolozenieI(0) == uderzajacy.getPolozenieI(0) and sortedList[j].getPolozenieI(1) == self.getPolozenieI(1): blackList.append(j)
                    if sortedList[j].getPolozenieI(0) == teoretyczna[0] and sortedList[j].getPolozenieI(1) == teoretyczna[1]: blackList.append(j)

            
            else:

                uderzony = self.getSwiat().findOrganizmByXY(0, 0, organizmy)

                uderzony = self.getSwiat().findOrganizmByXY(teoretyczna[0], teoretyczna[1], organizmy)

                if(uderzony != None and uderzony != organizmy[0]):

                    if uderzony.isPlant():
                        uderzony.kolizja(teoretyczna, blackList, sortedList, uderzony, uderzajacy, organizmy)

                    else:
                        self.kolizja(teoretyczna, blackList, sortedList, uderzony, uderzajacy, organizmy)

    #--------------------------------------------

    def kolizja(self, teoretyczna, blackList, sortedList, uderzony, uderzajacy, organizmy):

        lAtakujacego = self.getSwiat().sprawdzPole(self.getPolozenieI(0), self.getPolozenieI(1))
        lAtakowanego = self.getSwiat().sprawdzPole(teoretyczna[0], teoretyczna[1])

        blacklistAtakowany = [True]

        flag = True

        if lAtakujacego == lAtakowanego:

            self.getSwiat().rozmnazanie(organizmy, uderzajacy, uderzony)

            blacklistAtakowany[0] = False

        elif (not uderzajacy.ucieczka(teoretyczna, organizmy, blacklistAtakowany)):

            if(not uderzajacy.dobryWech(uderzony, blacklistAtakowany)):

                if(not uderzony.czyOdbito(uderzajacy, blacklistAtakowany)):

                    if(uderzony.czyJestTarczaAldura()):

                        uderzony.odstraszenieZPola(self.getPolozenie(), teoretyczna, organizmy, lAtakujacego)
                        flag = False

                    elif uderzajacy.czyJestTarczaAldura():

                        uderzajacy.odstraszenieZPola(teoretyczna, self.getPolozenie(), organizmy, lAtakowanego)
                        flag = False

                    if flag:

                        xUderzonego = teoretyczna[0]
                        yUderzonego = teoretyczna[1]

                        xUderzajacego = self.getPolozenieI(0)
                        yUderzajacego = self.getPolozenieI(1)

                        if uderzajacy.getSila() >= uderzony.getSila():

                            self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1), " ")

                            s = lAtakujacego

                            self.getSwiat().edytujPlansze(teoretyczna[0], teoretyczna[1], s)

                            self.getSwiat().deleteOrganizmByXY(teoretyczna[0], teoretyczna[1], organizmy)
                            self.getSwiat().changePositionOrganizm(self.getPolozenieI(0), self.getPolozenieI(1), teoretyczna[0], teoretyczna[1], organizmy)

                            temp = "Organizm " + lAtakujacego + " zaatakował z y: " + str(yUderzajacego) + " x: " + str(xUderzajacego) + " Organizm " + lAtakowanego + " który był na polu y: " + str(yUderzonego) + " x: " + str(xUderzonego) + " i zwyciężyl"

                            self.getSwiat().addToLog(temp)


                        if uderzajacy.getSila() < uderzony.getSila():

                            self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1), " ")

                            self.getSwiat().deleteOrganizmByXY(self.getPolozenieI(0), self.getPolozenieI(1), organizmy)

                            blacklistAtakowany[0] = False

                            temp = "Organizm " + uderzony.getZnak() + " będący na polu y: " + str(yUderzonego) + " x: " + str(xUderzonego) + " obronił się przed Organizmem " + uderzajacy.getZnak() + " ktory atakował z pola y: " + str(yUderzajacego) + " x: " + str(xUderzajacego)

                            self.getSwiat().addToLog(temp)


        for j in range(0, len(sortedList)):

            if sortedList[j].getPolozenieI(0) == self.getPolozenieI(0) and sortedList[j].getPolozenieI(1) == self.getPolozenieI(1): blackList.append(j)
            if sortedList[j].getPolozenieI(0) == teoretyczna[0] and sortedList[j].getPolozenieI(1) == teoretyczna[1] and blacklistAtakowany[0]: blackList.append(j)

