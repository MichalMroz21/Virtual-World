#pragma once
#include "Organizm.h"

class Roslina : public Organizm {

public:

	Roslina();

	Roslina(Organizm org);

	void akcja(std::vector<int>& blackList, std::vector<Organizm*>& sortedList, std::vector <std::vector <Organizm*> >& organizmy) override;

	void kolizja(std::vector<int> teoretyczna, std::vector<int>& blackList, std::vector<Organizm*>& sortedList, Organizm* uderzony, Organizm* uderzajacy, std::vector <std::vector <Organizm*>>& organizmy) override;

	void rysowanie() override;

	bool isPlant();

	char getZnak() override;

	bool czyZabojcza();

	int dodawanaSilaPoZjedzeniu();

	bool isRadioactive();

	~Roslina();

	int iloscRozp();
};