#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"

class Zolw : public Zwierze {

public:
	Zolw();
	Zolw(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Zolw(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	bool czyOdbito(Organizm* atakujacy);
	bool zmienPolozenie(Swiat* swiat);

	~Zolw();
};