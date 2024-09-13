from Zwierze import Zwierze

class Lis(Zwierze):
    
    def __init__(self):
        pass

    def __init__(self, swiat, poz, wiek, inicj, moc):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeWiek(wiek)
        super().changeInicjatywa(inicj)

        s = "L"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    def __init__(self, swiat, poz):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeInicjatywa(7)
        super().zmienSile(3)
        super().changeWiek(0)

        s = "L"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    #--------------------------------------------

    def rysowanie(self):
        print('L')

    def getZnak(self):
        return 'L'

    #--------------------------------------------

    def dobryWech(self, atakowany, blacklistAtakowany):
        if atakowany.getSila() > 3:
            atakowany.getSwiat().addToLog("Lis będący na polu y: " + str(self.getPolozenieI(1)) + " x: " + str(self.getPolozenieI(0)) + " wywęszył lepszy organizm " + atakowany.getZnak() + " na y: " + str(atakowany.getPolozenieI(1)) + " x: " + str(atakowany.getPolozenieI(0)))
            return True
        else:
            return False
