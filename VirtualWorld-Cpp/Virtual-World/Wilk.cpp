#include "Wilk.h"
#include "Zwierze.h"
#include <iostream>
#include "Organizm.h"

Wilk::Wilk()
{
}

Wilk::Wilk(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);

	getSwiat()->edytujPlansze(poz[0], poz[1], WILK);
}

Wilk::Wilk(Swiat* swiat, std::vector<unsigned int> poz)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(5);
	zmienSile(9);
	changeWiek(0);

	getSwiat()->edytujPlansze(poz[0], poz[1], WILK);
}

void Wilk::rysowanie()
{
	std::cout << WILK;
}

char Wilk::getZnak()
{
	return WILK;
}

Wilk::~Wilk()
{
}
