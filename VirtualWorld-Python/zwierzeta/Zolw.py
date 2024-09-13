from Zwierze import Zwierze
import random

class Zolw(Zwierze):
    
    def __init__(self):
        pass

    def __init__(self, swiat, poz, wiek, inicj, moc):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeWiek(wiek)
        super().changeInicjatywa(inicj)

        s = "Z"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    def __init__(self, swiat, poz):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeInicjatywa(1)
        super().zmienSile(2)
        super().changeWiek(0)

        s = "Z"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    #--------------------------------------------

    def rysowanie(self):
        print('Z')

    def getZnak(self):
        return 'Z'

    #--------------------------------------------

    def czyOdbito(self, atakujacy, blacklistAtakowany):

        if atakujacy.getSila() < 5:
            blacklistAtakowany[0] = False
            atakujacy.getSwiat().addToLog("Zółw będący na polu y: " + str(self.getPolozenieI(1)) + " x: " + str(self.getPolozenieI(0)) + " odbił obrażenia od organizmu " + atakujacy.getZnak() + " z pola y: " + str(atakujacy.getPolozenieI(1)) + " x: " + str(atakujacy.getPolozenieI(0)) )
            return True

        else:
            return False

    #--------------------------------------------

    def zmienPolozenie(self, swiat):
        r = random.randrange(0, 4)

        if r <= 2:
            swiat.addToLog("Żółw będący na polu y: " + str(self.getPolozenieI(1)) + " x: " + str(self.getPolozenieI(0)) + " nie wykonał ruchu!")
            return False

        else:
            return True
