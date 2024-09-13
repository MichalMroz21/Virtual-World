#pragma once
#include <vector>
#include "Swiat.h"

class Swiat;

class Organizm {

	friend Swiat;

private:

	Swiat* swiat;

	std::vector<int> polozenie;

	int sila, inicjatywa, wiek;
	

public:

	int getInicjatywa();

	void changeInicjatywa(int i);

	void changeWiek(int i);

	int getWiek();

	int getPolozenie(int i);

	std::vector<int>& getPolozenie();

	void changePolozenie(int x, int y);

	Swiat* getSwiat();

	void changeSwiat(Swiat* swiat);

	Organizm();

	~Organizm();

	virtual void akcja(std::vector<int>& blackList, std::vector<Organizm*>& sortedList, std::vector <std::vector <Organizm*> >& organizmy);

	virtual void kolizja(std::vector<int> teoretyczna, std::vector<int>& blackList, std::vector<Organizm*>& sortedList, Organizm* uderzony, Organizm* uderzajacy, std::vector <std::vector <Organizm*>>& organizmy);

	virtual void rysowanie();

	virtual char getZnak();

	virtual bool czyOdbito(Organizm* atakujacy);

	virtual bool zmienPolozenie(Swiat* swiat);

	virtual bool dobryWech(Organizm* atakowany);

	virtual int zasieg();

	virtual bool isPlant();

	virtual int iloscRozp();

	virtual bool ucieczka(std::vector<int>& teoretyczna, std::vector <std::vector <Organizm*>>& organizmy);

	virtual void odstraszenieZPola(std::vector<int>& poleAtakujacego, std::vector<int>& poleAtakowanego, std::vector <std::vector <Organizm*>>& organizmy, char odstraszonego);

	virtual int dodawanaSilaPoZjedzeniu();

	virtual bool czyZabojcza();

	virtual bool isRadioactive();

	virtual int getKierunekRuchu();
	virtual void zmienKierunekRuchu(int a);

	virtual void podajKierunekRuchu();

	virtual void podajInfoTarcza(int tura);

	virtual bool czyJestTarczaAldura();

	virtual void zmienStanTarczyAldura(bool b);

	int getSila();

	void zmienSile(int s);
};