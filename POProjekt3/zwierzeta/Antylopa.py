from Zwierze import Zwierze
import random

class Antylopa(Zwierze):
    
    def __init__(self):
        pass

    def __init__(self, swiat, poz, wiek, inicj, moc):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeWiek(wiek)
        super().changeInicjatywa(inicj)

        s = "A"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    def __init__(self, swiat, poz):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeInicjatywa(4)
        super().zmienSile(4)
        super().changeWiek(0)

        s = "A"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    #--------------------------------------------

    def rysowanie(self):
        print('A')

    def getZnak(self):
        return 'A'

    #--------------------------------------------

    def zasieg(self):
        return 2

    #--------------------------------------------

    def ucieczka(self, teoretyczna, organizmy, blacklistAtakowany):

        r = random.randrange(0, 2)

        s = self.getZnak()

        if r >= 1:

            blacklistAtakowany[0] = False

            self.getSwiat().addToLog("Antylopa z pola y: " + str(self.getPolozenieI(1)) + " x: " + str(self.getPolozenieI(0)) + " uciekła przed walką z organizmem " + str(self.getSwiat().sprawdzPole(teoretyczna[0], teoretyczna[1])) + " y: " + str(teoretyczna[1]) + " x: " + str(teoretyczna[0])) 

            if teoretyczna[1] - 1 >= 0 and self.getSwiat().sprawdzPole(teoretyczna[0], teoretyczna[1] - 1) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1), " ")
                    self.getSwiat().edytujPlansze(teoretyczna[0], teoretyczna[1] - 1, s)
                    self.getSwiat().changePositionOrganizm(self.getPolozenieI(0), self.getPolozenieI(1), teoretyczna[0], teoretyczna[1] - 1, organizmy)
            
            elif teoretyczna[1] + 1 < self.getSwiat().getRozmiarY() and self.getSwiat().sprawdzPole(teoretyczna[0], teoretyczna[1] + 1) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1), " ")
                    self.getSwiat().edytujPlansze(teoretyczna[0], teoretyczna[1] + 1, s)
                    self.getSwiat().changePositionOrganizm(self.getPolozenieI(0), self.getPolozenieI(1), teoretyczna[0], teoretyczna[1] + 1, organizmy)


            elif teoretyczna[0] - 1 >= 0 and self.getSwiat().sprawdzPole(teoretyczna[0] - 1, teoretyczna[1]) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1), " ")
                    self.getSwiat().edytujPlansze(teoretyczna[0] - 1, teoretyczna[1], s)
                    self.getSwiat().changePositionOrganizm(self.getPolozenieI(0), self.getPolozenieI(1), teoretyczna[0] - 1, teoretyczna[1], organizmy)


            elif teoretyczna[0] + 1 < self.getSwiat().getRozmiarX() and self.getSwiat().sprawdzPole(teoretyczna[0] + 1, teoretyczna[1]) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1), " ")
                    self.getSwiat().edytujPlansze(teoretyczna[0] + 1, teoretyczna[1], s)
                    self.getSwiat().changePositionOrganizm(self.getPolozenieI(0), self.getPolozenieI(1), teoretyczna[0] + 1, teoretyczna[1], organizmy)


            if self.getSwiat().getIsHex():

                if teoretyczna[1] - 1 >= 0 and teoretyczna[0] + 1 < self.getSwiat().getRozmiarX() and self.getSwiat().sprawdzPole(teoretyczna[0] + 1, teoretyczna[1] - 1) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1), " ")
                    self.getSwiat().edytujPlansze(teoretyczna[0] + 1, teoretyczna[1] - 1, s)
                    self.getSwiat().changePositionOrganizm(self.getPolozenieI(0), self.getPolozenieI(1), teoretyczna[0] + 1, teoretyczna[1] - 1, organizmy)
            
                elif teoretyczna[1] + 1 < self.getSwiat().getRozmiarY() and teoretyczna[0] - 1 >= 0 and self.getSwiat().sprawdzPole(teoretyczna[0] - 1, teoretyczna[1] + 1) == ' ':
                    self.getSwiat().edytujPlansze(self.getPolozenieI(0), self.getPolozenieI(1), " ")
                    self.getSwiat().edytujPlansze(teoretyczna[0] - 1, teoretyczna[1] + 1, s)
                    self.getSwiat().changePositionOrganizm(self.getPolozenieI(0), self.getPolozenieI(1), teoretyczna[0] - 1, teoretyczna[1] + 1, organizmy)

            return True

        return False

    #--------------------------------------------

