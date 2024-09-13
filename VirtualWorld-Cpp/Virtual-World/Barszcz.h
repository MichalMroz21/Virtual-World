#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"
#include "Roslina.h"

class Barszcz : public Roslina {

public:
	Barszcz();
	Barszcz(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Barszcz(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	bool czyZabojcza();

	bool isRadioactive();

	~Barszcz();
};
