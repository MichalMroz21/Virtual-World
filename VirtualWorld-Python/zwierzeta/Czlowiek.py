from Zwierze import Zwierze

class Czlowiek(Zwierze):
    
    def __init__(self):
        pass

    def __init__(self, swiat, poz, wiek, inicj, moc):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeWiek(wiek)
        super().changeInicjatywa(inicj)

        self.__kierunekRuchu = 0
        self.__tarczaAldura = False

        s = "C"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    def __init__(self, swiat, poz):

        super(Zwierze, self).__init__()

        super().changeSwiat(swiat)
        super().changePolozenie(poz[0], poz[1])
        super().changeInicjatywa(4)
        super().zmienSile(5)
        super().changeWiek(0)

        self.__kierunekRuchu = 0
        self.__tarczaAldura = False

        s = "C"
        super().getSwiat().edytujPlansze(poz[0], poz[1], s)

    #--------------------------------------------

    def rysowanie(self):
        print('C')

    def getZnak(self):
        return 'C'

    #--------------------------------------------

    def podajKierunekRuchu(self):
        s = ""
        print("Czlowiek bedzie poruszal sie w: ", end='')
        s += "Czlowiek bedzie poruszal sie w: "

        if self.__kierunekRuchu == 0:
            print("Okresl kierunek ruchu klikajac odpowiednia strzalke na klawiaturze!")
            s += "Okresl kierunek ruchu klikajac odpowiednia strzalke na klawiaturze!"

        elif self.__kierunekRuchu == 1:
            print("gore")
            s += "gore"

        elif self.__kierunekRuchu == 2:
            print("dol")
            s += "dol"

        elif self.__kierunekRuchu == 3:
            print("lewo")
            s += "lewo"

        elif self.__kierunekRuchu == 4:
            print("prawo")
            s += "prawo"

        return s

    #--------------------------------------------

    def podajInfoTarcza(self, tura):
        ret = ""
        if self.__tarczaAldura:
           # print("Tarcza aktywowana! Pozostalo tur: " + str(tura), end='')
            ret += "Tarcza aktywowana! Pozostało tur: " + str(tura)

        else:
            if tura == -5:
                #print("Mozna aktywowac tarcze!", end='')
                ret += "Można aktywować tarczę!"

            else:
                #print("Tarcza ma cooldown! Mozna aktywowac za: " + str(5 + tura) + " tur!", end='')
                ret += "Tarcza musi się odnowić! Mozna aktywować za: " + str(5 + tura) + " tur!"

        return ret

    #--------------------------------------------

    def odstraszenieZPola(self, poleAtakujacego, poleAtakowanego, organizmy, odstraszonego):

        flag = False

        xAtakujacego = poleAtakujacego[0]
        yAtakujacego = poleAtakujacego[1]

        xAtakowanego = poleAtakowanego[0]
        yAtakowanego = poleAtakowanego[1]

        Odstraszonego = "" + odstraszonego

        if poleAtakowanego[1] - 1 >= 0 and self.getSwiat().sprawdzPole(poleAtakowanego[0], poleAtakowanego[1] - 1) == ' ':
            self.getSwiat().edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], " ")
            self.getSwiat().edytujPlansze(poleAtakowanego[0], poleAtakowanego[1] - 1, Odstraszonego)
            self.getSwiat().changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0], poleAtakowanego[1] - 1, organizmy)
            flag = True;


        elif poleAtakowanego[1] + 1 < self.getSwiat().getRozmiarY() and self.getSwiat().sprawdzPole(poleAtakowanego[0], poleAtakowanego[1] + 1) == ' ':
            self.getSwiat().edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], " ")
            self.getSwiat().edytujPlansze(poleAtakowanego[0], poleAtakowanego[1] + 1, Odstraszonego)
            self.getSwiat().changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0], poleAtakowanego[1] + 1, organizmy)
            flag = True
        

        elif poleAtakowanego[0] - 1 >= 0 and self.getSwiat().sprawdzPole(poleAtakowanego[0] - 1, poleAtakowanego[1]) == ' ':
            self.getSwiat().edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], " ")
            self.getSwiat().edytujPlansze(poleAtakowanego[0] - 1, poleAtakowanego[1], Odstraszonego)
            self.getSwiat().changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0] - 1, poleAtakowanego[1], organizmy)
            flag = True
        

        elif poleAtakowanego[0] + 1 < self.getSwiat().getRozmiarX() and self.getSwiat().sprawdzPole(poleAtakowanego[0] + 1, poleAtakowanego[1]) == ' ':
            self.getSwiat().edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], " ")
            self.getSwiat().edytujPlansze(poleAtakowanego[0] + 1, poleAtakowanego[1], Odstraszonego)
            self.getSwiat().changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0] + 1, poleAtakowanego[1], organizmy)
            flag = True

        if self.getSwiat().getIsHex():

            if poleAtakowanego[1] - 1 >= 0 and poleAtakowanego[0] + 1 < self.getSwiat().getRozmiarX() and self.getSwiat().sprawdzPole(poleAtakowanego[0] + 1, poleAtakowanego[1] - 1) == ' ':
                self.getSwiat().edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], " ")
                self.getSwiat().edytujPlansze(poleAtakowanego[0] + 1, poleAtakowanego[1] - 1, Odstraszonego)
                self.getSwiat().changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0] + 1, poleAtakowanego[1] - 1, organizmy)
                flag = True;


            elif poleAtakowanego[1] + 1 < self.getSwiat().getRozmiarY() and poleAtakowanego[0] - 1 >= 0 and self.getSwiat().sprawdzPole(poleAtakowanego[0] - 1, poleAtakowanego[1] + 1) == ' ':
                self.getSwiat().edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], " ")
                self.getSwiat().edytujPlansze(poleAtakowanego[0] - 1, poleAtakowanego[1] + 1, Odstraszonego)
                self.getSwiat().changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0] - 1, poleAtakowanego[1] + 1, organizmy)
                flag = True

        if flag:
            temp = "Człowiek odstraszył zwierzę " + odstraszonego + " z y: " + str(yAtakujacego) + " x: " + str(xAtakujacego) + " tarczą Aldura!"
            self.getSwiat().addToLog(temp)

        else:
            temp = "Czlowiek odstraszył zwierzę (" + odstraszonego + ") tarczą Aldura ale zwierze nie miało gdzie uciec!"
            self.getSwiat().addToLog(temp)

    #--------------------------------------------

    def zmienStanTarczyAldura(self, b):
        self.__tarczaAldura = b

    #--------------------------------------------

    def czyJestTarczaAldura(self):
        return self.__tarczaAldura

    #--------------------------------------------

    def zmienKierunekRuchu(self, a):
        self.__kierunekRuchu = a

    #--------------------------------------------

    def getKierunekRuchu(self):
        return self.__kierunekRuchu
