#include "Owca.h"
#include "Zwierze.h"
#include <iostream>
#include "Organizm.h"
#include "Trawa.h"
#include "Roslina.h"
#include "Mlecz.h"

Mlecz::Mlecz()
{
}

Mlecz::Mlecz(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);

	getSwiat()->edytujPlansze(poz[0], poz[1], MLECZ);
}

Mlecz::Mlecz(Swiat* swiat, std::vector<unsigned int> poz)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(0);
	zmienSile(0);
	changeWiek(0);

	getSwiat()->edytujPlansze(poz[0], poz[1], MLECZ);
}

void Mlecz::rysowanie()
{
	std::cout << MLECZ;
}

char Mlecz::getZnak()
{
	return MLECZ;
}

int Mlecz::iloscRozp()
{
	return 3;
}

Mlecz::~Mlecz()
{
}