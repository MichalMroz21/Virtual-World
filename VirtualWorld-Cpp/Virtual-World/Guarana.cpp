#include "Owca.h"
#include "Zwierze.h"
#include <iostream>
#include "Organizm.h"
#include "Trawa.h"
#include "Roslina.h"
#include "Guarana.h"

Guarana::Guarana()
{
}

Guarana::Guarana(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);

	getSwiat()->edytujPlansze(poz[0], poz[1], GUARANA);
}

Guarana::Guarana(Swiat* swiat, std::vector<unsigned int> poz)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(0);
	zmienSile(0);
	changeWiek(0);

	getSwiat()->edytujPlansze(poz[0], poz[1], GUARANA);
}

void Guarana::rysowanie()
{
	std::cout << GUARANA;
}

char Guarana::getZnak()
{
	return GUARANA;
}

int Guarana::dodawanaSilaPoZjedzeniu()
{
	return 3;
}

Guarana::~Guarana()
{
}