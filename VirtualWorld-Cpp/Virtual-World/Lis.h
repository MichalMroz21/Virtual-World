#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"

class Lis : public Zwierze {

public:
	Lis();
	Lis(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Lis(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	bool dobryWech(Organizm* atakowany);

	~Lis();
};