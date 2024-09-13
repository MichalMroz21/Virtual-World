#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"

class Owca : public Zwierze {

public:
	Owca();
	Owca(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Owca(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	~Owca();
};