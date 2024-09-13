#include "Zolw.h"
#include <iostream>

Zolw::Zolw()
{
}

Zolw::Zolw(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{

	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);

	getSwiat()->edytujPlansze(poz[0], poz[1], ZOLW);

}

Zolw::Zolw(Swiat* swiat, std::vector<unsigned int> poz)
{

	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(1);
	zmienSile(2);
	changeWiek(0);

	getSwiat()->edytujPlansze(poz[0], poz[1], ZOLW);

}

void Zolw::rysowanie()
{
	std::cout << ZOLW;
}

char Zolw::getZnak()
{
	return ZOLW;
}

bool Zolw::czyOdbito(Organizm* atakujacy)
{
	if (atakujacy->getSila() < 5) {
		getSwiat()->addToLog("Jeden z zolwi odbil obrazenia!");
		return true;
	}
	else return false;
}

bool Zolw::zmienPolozenie(Swiat* swiat)
{
	int temp = rand() % 4;
	if (temp <= 2) {
		swiat->addToLog("Jeden z zolwi nie ruszyl sie!"); 
		return false;
	}
	else return true;
}

Zolw::~Zolw()
{
}
