from Zwierze import Zwierze

class Wilk(Zwierze):
    
    def __init__(self):
        pass

    def __init__(self, swiat, poz, wiek, inicj, moc):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeWiek(wiek)
        super().changeInicjatywa(inicj)

        s = "W"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    def __init__(self, swiat, poz):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeInicjatywa(5)
        super().zmienSile(9)
        super().changeWiek(0)

        s = "W"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    #--------------------------------------------

    def rysowanie(self):
        print('W')

    def getZnak(self):
        return 'W'
