#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"

class Wilk : public Zwierze {

public:
	Wilk();
	Wilk(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Wilk(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	~Wilk();
};