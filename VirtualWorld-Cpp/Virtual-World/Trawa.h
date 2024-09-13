#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"
#include "Roslina.h"

class Trawa : public Roslina {

public:
	Trawa();
	Trawa(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Trawa(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	~Trawa();
};