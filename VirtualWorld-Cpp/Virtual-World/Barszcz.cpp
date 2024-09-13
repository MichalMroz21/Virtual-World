#include "Owca.h"
#include "Zwierze.h"
#include <iostream>
#include "Organizm.h"
#include "Trawa.h"
#include "Roslina.h"
#include "Jagody.h"
#include "Barszcz.h"
#include "DEF.h"

Barszcz::Barszcz()
{
}

Barszcz::Barszcz(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);

	getSwiat()->edytujPlansze(poz[0], poz[1], BARSZCZ);
}

Barszcz::Barszcz(Swiat* swiat, std::vector<unsigned int> poz)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(0);
	zmienSile(10);
	changeWiek(0);

	getSwiat()->edytujPlansze(poz[0], poz[1], BARSZCZ);
}

void Barszcz::rysowanie()
{
	std::cout << BARSZCZ;
}

char Barszcz::getZnak()
{
	return BARSZCZ;
}

bool Barszcz::czyZabojcza()
{
	return 1;
}

bool Barszcz::isRadioactive()
{
	return 1;
}

Barszcz::~Barszcz()
{
}