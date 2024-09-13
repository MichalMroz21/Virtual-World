#include "Owca.h"
#include "Zwierze.h"
#include <iostream>
#include "Organizm.h"
#include "Trawa.h"
#include "Roslina.h"
#include "Jagody.h"

Jagody::Jagody()
{
}

Jagody::Jagody(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);

	getSwiat()->edytujPlansze(poz[0], poz[1], JAGODY);
}

Jagody::Jagody(Swiat* swiat, std::vector<unsigned int> poz)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(0);
	zmienSile(99);
	changeWiek(0);

	getSwiat()->edytujPlansze(poz[0], poz[1], JAGODY);
}

void Jagody::rysowanie()
{
	std::cout << JAGODY;
}

char Jagody::getZnak()
{
	return JAGODY;
}

bool Jagody::czyZabojcza()
{
	return 1;
}

Jagody::~Jagody()
{
}