#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"

class Antylopa : public Zwierze {

public:
	Antylopa();
	Antylopa(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Antylopa(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	int zasieg();

	bool ucieczka(std::vector<int>& teoretyczna, std::vector <std::vector <Organizm*>>& organizmy);

	~Antylopa();
};
