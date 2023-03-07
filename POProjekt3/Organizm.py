class Organizm():
 
    def __init__(self):
        self.__polozenie = [0, 0]
        self.__inicjatywa = 0
        self.__wiek = 0
        self.__swiat = None
        self.__sila = 0

    def getInicjatywa(self):
        return self.__inicjatywa

    def changeInicjatywa(self, i):
        self.__inicjatywa = i

    def changeWiek(self, i):
        self.__wiek = i

    def getWiek(self):
        return self.__wiek

    def addOneToWiek(self):
        self.__wiek += 1

    def getPolozenieI(self, i):
        return self.__polozenie[i]

    def getPolozenie(self):
        return self.__polozenie

    def changePolozenie(self, x, y):
        self.__polozenie[0] = x
        self.__polozenie[1] = y

    def getSwiat(self):
        return self.__swiat

    def changeSwiat(self, swiat):
        self.__swiat = swiat

    def getZnak(self):
        return 0

    def czyOdbito(self, atakujacy, blacklistAtakowany):
        return False

    def zmienPolozenie(self, swiat):
        return True
    
    def dobryWech(self, atakowany, blacklistAtakowany):
        return False

    def zasieg(self):
        return 1

    def isPlant(self):
        return False

    def iloscRozp(self):
        return 1

    def ucieczka(self, teoretyczna, organizmy, blacklistAtakowany):
        return False

    def odstraszenieZPola(self, poleAtakujacego, poleAtakowanego, organizmy, odstraszonego):
        pass

    def dodawanaSilaPoZjedzeniu(self):
        return 0

    def czyZabojcza(self):
        return False

    def isRadioactive(self):
        return False

    def isCyber(self):
        return False

    def getKierunekRuchu(self):
        return 0

    def zmienKierunekRuchu(self, a):
        pass

    def podajKierunekRuchu(self):
        return None

    def podajInfoTarcza(self, tura):
        return None

    def czyJestTarczaAldura(self):
        return False

    def zmienStanTarczyAldura(self, b):
        pass

    def getSila(self):
        return self.__sila

    def zmienSile(self, s):
        self.__sila = s

    def rysowanie(self):
        pass

    def akcja(self, blackList, sortedList, organizmy):
        pass

    def kolizja(self, teoretyczna, blackList, sortedList, uderzony, uderzajacy, organizmy):
        pass







