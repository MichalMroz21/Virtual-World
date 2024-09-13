#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"
#include "Roslina.h"

class Mlecz : public Roslina {

public:
	Mlecz();
	Mlecz(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Mlecz(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	int iloscRozp();

	~Mlecz();
};
