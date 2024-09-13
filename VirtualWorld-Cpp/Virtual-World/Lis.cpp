#include "Owca.h"
#include "Zwierze.h"
#include <iostream>
#include "Organizm.h"
#include "Lis.h"

Lis::Lis()
{
}

Lis::Lis(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);

	getSwiat()->edytujPlansze(poz[0], poz[1], LIS);
}

Lis::Lis(Swiat* swiat, std::vector<unsigned int> poz)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(7);
	changeWiek(0);

	getSwiat()->edytujPlansze(poz[0], poz[1], LIS);
}

void Lis::rysowanie()
{
	std::cout << LIS;
}

char Lis::getZnak()
{
	return LIS;
}

bool Lis::dobryWech(Organizm* atakowany)
{
	if (atakowany->getSila() > 3) {
		getSwiat()->addToLog("Jeden z lisow wyweszyl lepszy organizm!");
		return true;
	}
	else return false;
}

Lis::~Lis()
{
}