#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"
#include "Roslina.h"

class Jagody : public Roslina {

public:
	Jagody();
	Jagody(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Jagody(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	bool czyZabojcza();

	~Jagody();
};