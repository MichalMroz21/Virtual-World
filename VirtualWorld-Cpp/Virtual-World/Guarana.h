#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"
#include "Roslina.h"

class Guarana : public Roslina {

public:
	Guarana();
	Guarana(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Guarana(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	int dodawanaSilaPoZjedzeniu();

	~Guarana();
};