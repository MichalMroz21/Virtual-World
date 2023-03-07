from Roslina import Roslina

class Jagody(Roslina):
    
    def __init__(self):
        pass

    def __init__(self, swiat, poz, wiek, inicj, moc):

        super(Roslina, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeWiek(wiek)
        super().changeInicjatywa(inicj)

        s = "J"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    def __init__(self, swiat, poz):

        super(Roslina, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeInicjatywa(0)
        super().zmienSile(99)
        super().changeWiek(0)

        s = "J"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    #--------------------------------------------

    def rysowanie(self):
        print('J')

    def getZnak(self):
        return 'J'

    def czyZabojcza(self):
        return True



