#include "Owca.h"
#include "Zwierze.h"
#include <iostream>
#include "Organizm.h"

Owca::Owca()
{
}

Owca::Owca(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);

	getSwiat()->edytujPlansze(poz[0], poz[1], OWCA);
}

Owca::Owca(Swiat* swiat, std::vector<unsigned int> poz)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(4);
	zmienSile(4);
	changeWiek(0);

	getSwiat()->edytujPlansze(poz[0], poz[1], OWCA);
}

void Owca::rysowanie()
{
	std::cout << OWCA;
}

char Owca::getZnak()
{
	return OWCA;
}

Owca::~Owca()
{
}