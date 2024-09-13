#pragma once
#include "Organizm.h"

class Zwierze : public Organizm {

public:

	Zwierze();

	Zwierze(Organizm org);

	void akcja(std::vector<int>& blackList, std::vector<Organizm*>& sortedList, std::vector <std::vector <Organizm*> >& organizmy) override;

	void kolizja(std::vector<int> teoretyczna, std::vector<int>& blackList, std::vector<Organizm*>& sortedList, Organizm* uderzony, Organizm* uderzajacy, std::vector <std::vector <Organizm*>>& organizmy) override;

	void rysowanie() override;

    char getZnak() override;

	bool czyOdbito(Organizm* atakujacy);

	bool dobryWech(Organizm* atakowany);

	bool zmienPolozenie(Swiat* swiat);

	bool isPlant();

	int zasieg();

	bool ucieczka(std::vector<int>& teoretyczna, std::vector <std::vector <Organizm*>>& organizmy);

	void odstraszenieZPola(std::vector<int>& poleAtakujacego, std::vector<int>& poleAtakowanego, std::vector <std::vector <Organizm*>>& organizmy, char odstraszonego);

	int getKierunekRuchu();
	void zmienKierunekRuchu(int a);

	void podajKierunekRuchu();

	void podajInfoTarcza(int tura);

	void zmienStanTarczyAldura(bool b);

	bool czyJestTarczaAldura();

	~Zwierze();


};