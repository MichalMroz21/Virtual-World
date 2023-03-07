from Organizm import Organizm
import random

class Roslina(Organizm):
    
    def __init__(self):
        super(Organizm, self).__init__()

    def __init__(self, org):
        super(Organizm, self).__init__()

    #--------------------------------------------

    def rysowanie(self):
        print('R')

    def getZnak(self):
        print('R')

    def isPlant(self):
        return True 

    def czyZabojcza(self):
        return False 

    def dodawanaSilaPoZjedzeniu(self):
        return 0 

    def isRadioactive(self):
        return False 

    def iloscRozp(self):
        return 1

    #--------------------------------------------

    def akcja(self, blackList, sortedList, organizmy):
        
        if self.isRadioactive():
            self.getSwiat().usunWokol(self.getPolozenieI(0), self.getPolozenieI(1), organizmy, self)

        czySieRozprzestrzenilaRaz = False

        for i in range(0, self.iloscRozp()):

            r = random.randrange(0, 4)

            if r == 0:

                teoretyczna = [0, 0]

                x = 0
                y = 0

                s = self.getZnak()
                czySieWykonalo = False

                if self.getPolozenieI(1) - 1 >= 0 and self.getSwiat().sprawdzPole(self.getPolozenieI(0), self.getPolozenieI(1) - 1) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1) - 1, s)
                    self.getSwiat().addOrganizmByXY(self.getPolozenieI(0), self.getPolozenieI(1) - 1, organizmy, self.getZnak())
                    x = self.getPolozenieI(0)
                    y = self.getPolozenieI(1) - 1
                    czySieWykonalo = True
                    czySieRozprzestrzenilaRaz = True


                elif self.getPolozenieI(1) + 1 < self.getSwiat().getRozmiarY() and self.getSwiat().sprawdzPole(self.getPolozenieI(0), self.getPolozenieI(1) + 1) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1) + 1, s)
                    self.getSwiat().addOrganizmByXY(self.getPolozenieI(0), self.getPolozenieI(1) + 1, organizmy, self.getZnak())
                    x = self.getPolozenieI(0)
                    y = self.getPolozenieI(1) + 1
                    czySieWykonalo = True
                    czySieRozprzestrzenilaRaz = True


                elif self.getPolozenieI(0) - 1 >= 0 and self.getSwiat().sprawdzPole(self.getPolozenieI(0) - 1, self.getPolozenieI(1)) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0) - 1, self.getPolozenieI(1), s)
                    self.getSwiat().addOrganizmByXY(self.getPolozenieI(0) - 1, self.getPolozenieI(1), organizmy, self.getZnak())
                    x = self.getPolozenieI(0) - 1
                    y = self.getPolozenieI(1)
                    czySieWykonalo = True
                    czySieRozprzestrzenilaRaz = True


                elif self.getPolozenieI(0) + 1 < self.getSwiat().getRozmiarX() and self.getSwiat().sprawdzPole(self.getPolozenieI(0) + 1, self.getPolozenieI(1)) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0) + 1, self.getPolozenieI(1), s)
                    self.getSwiat().addOrganizmByXY(self.getPolozenieI(0) + 1, self.getPolozenieI(1), organizmy, self.getZnak())
                    x = self.getPolozenieI(0) + 1
                    y = self.getPolozenieI(1)
                    czySieWykonalo = True
                    czySieRozprzestrzenilaRaz = True


                if self.getSwiat().getIsHex():

                    if self.getPolozenieI(1) - 1 >= 0 and self.getPolozenieI(0) + 1 < self.getSwiat().getRozmiarX() and self.getSwiat().sprawdzPole(self.getPolozenieI(0) + 1, self.getPolozenieI(1) - 1) == ' ':
                        self.getSwiat().edytujPlansze(self.getPolozenieI(0) + 1, self.getPolozenieI(1) - 1, s)
                        self.getSwiat().addOrganizmByXY(self.getPolozenieI(0) + 1, self.getPolozenieI(1) - 1, organizmy, self.getZnak())
                        x = self.getPolozenieI(0) + 1
                        y = self.getPolozenieI(1) - 1
                        czySieWykonalo = True
                        czySieRozprzestrzenilaRaz = True


                    elif self.getPolozenieI(1) + 1 < self.getSwiat().getRozmiarY() and self.getPolozenieI(0) - 1 >= 0 and self.getSwiat().sprawdzPole(self.getPolozenieI(0) - 1, self.getPolozenieI(1) + 1) == ' ':
                        self.getSwiat().edytujPlansze(self.getPolozenieI(0) - 1, self.getPolozenieI(1) + 1, s)
                        self.getSwiat().addOrganizmByXY(self.getPolozenieI(0) - 1, self.getPolozenieI(1) + 1, organizmy, self.getZnak())
                        x = self.getPolozenieI(0) - 1
                        y = self.getPolozenieI(1) + 1
                        czySieWykonalo = True
                        czySieRozprzestrzenilaRaz = True
                

                if czySieWykonalo:

                    temp = "Roślina " + self.getZnak() + " będąca na polu y: " + str(self.getPolozenieI(1)) + " x: " + str(self.getPolozenieI(0)) + " rozprzestrzeniła się na pole y: " + str(y) + " x: " + str(x)

                    self.getSwiat().addToLog(temp)

        if not czySieRozprzestrzenilaRaz:

            temp = "Roślina " + self.getZnak() + " będąca na polu y: " + str(self.getPolozenieI(1)) + " x: " + str(self.getPolozenieI(0)) + " nigdzie się nie rozprzestrzeniła "

            self.getSwiat().addToLog(temp)

     
    #--------------------------------------------

    def kolizja(self, teoretyczna, blackList, sortedList, uderzony, uderzajacy, organizmy):

        lAtakujacego = uderzajacy.getZnak();
        if self.czyZabojcza(): 

            x = uderzajacy.getPolozenieI(0)
            y = uderzajacy.getPolozenieI(1)

            if uderzajacy.isCyber():

                self.getSwiat().edytujPlansze(uderzajacy.getPolozenieI(0), uderzajacy.getPolozenieI(1), " ")
                self.getSwiat().deleteOrganizmByXY(teoretyczna[0], teoretyczna[1], organizmy)
                self.getSwiat().changePositionOrganizm(uderzajacy.getPolozenieI(0), uderzajacy.getPolozenieI(1), teoretyczna[0], teoretyczna[1], organizmy)
            
                self.getSwiat().edytujPlansze(teoretyczna[0], teoretyczna[1], uderzajacy.getZnak())

            else:

                self.getSwiat().edytujPlansze(uderzajacy.getPolozenieI(0), uderzajacy.getPolozenieI(1), " ")
                self.getSwiat().deleteOrganizmByXY(uderzajacy.getPolozenieI(0), uderzajacy.getPolozenieI(1), organizmy)
            
                self.getSwiat().edytujPlansze(teoretyczna[0], teoretyczna[1], " ")
                self.getSwiat().deleteOrganizmByXY(teoretyczna[0], teoretyczna[1], organizmy)

            temp = "Zwierze " + uderzajacy.getZnak() + " z pola y: " + str(y) + " x: " + str(x) + " zjadło śmiertelną roślinę " + uderzony.getZnak() + " która była na polu y: " + str(teoretyczna[1]) + " x: " + str(teoretyczna[0])

            self.getSwiat().addToLog(temp)

        else: 

            x = uderzajacy.getPolozenieI(0)
            y = uderzajacy.getPolozenieI(1)

            self.getSwiat().edytujPlansze(uderzajacy.getPolozenieI(0), uderzajacy.getPolozenieI(1), " ")
            s = lAtakujacego
            self.getSwiat().edytujPlansze(teoretyczna[0], teoretyczna[1], s)

            self.getSwiat().deleteOrganizmByXY(teoretyczna[0], teoretyczna[1], organizmy)
            self.getSwiat().changePositionOrganizm(uderzajacy.getPolozenieI(0), uderzajacy.getPolozenieI(1), teoretyczna[0], teoretyczna[1], organizmy)

            self.getSwiat().zmienSileByXY(uderzajacy.getPolozenieI(0), uderzajacy.getPolozenieI(1), organizmy, uderzony.dodawanaSilaPoZjedzeniu())

            if uderzony.dodawanaSilaPoZjedzeniu() > 0:
                temp = "Organizm " + uderzajacy.getZnak() + " z pola y: " + str(y) + " x: " + str(x) + " zjadł roślinę " + uderzony.getZnak() + " która była na polu y: " + str(teoretyczna[1]) + " x: " + str(teoretyczna[0]) + " i zwiększył swoją siłę o " + str(uderzony.dodawanaSilaPoZjedzeniu())

                self.getSwiat().addToLog(temp)

            else:
                temp = "Organizm " + uderzajacy.getZnak() + " z pola y: " + str(y) + " x: " + str(x) + " zjadł roślinę " + uderzony.getZnak() + " która była na polu y: " + str(teoretyczna[1]) + " x: " + str(teoretyczna[0])

                self.getSwiat().addToLog(temp)


        for j in range(0, len(sortedList)):

            if sortedList[j].getPolozenieI(0) == uderzajacy.getPolozenieI(0) and sortedList[j].getPolozenieI(1) == uderzajacy.getPolozenieI(1):   blackList.append(j)
            if sortedList[j].getPolozenieI(0) == teoretyczna[0] and sortedList[j].getPolozenieI(1) == teoretyczna[1] and (not self.czyZabojcza()):   blackList.append(j)

    #--------------------------------------------