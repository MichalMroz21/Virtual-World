#include "Owca.h"
#include "Zwierze.h"
#include <iostream>
#include "Organizm.h"
#include "Antylopa.h"

Antylopa::Antylopa()
{
}

Antylopa::Antylopa(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);

	getSwiat()->edytujPlansze(poz[0], poz[1], ANTYLOPA);
}

Antylopa::Antylopa(Swiat* swiat, std::vector<unsigned int> poz)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(4);
	zmienSile(4);
	changeWiek(0);

	getSwiat()->edytujPlansze(poz[0], poz[1], ANTYLOPA);
}

void Antylopa::rysowanie()
{
	std::cout << ANTYLOPA;
}

char Antylopa::getZnak()
{
	return ANTYLOPA;
}

int Antylopa::zasieg()
{
	return 2;
}

bool Antylopa::ucieczka(std::vector<int>& teoretyczna, std::vector <std::vector <Organizm*>>& organizmy)
{

	int temp = rand() % 2;

	if (temp) {
		getSwiat()->addToLog("Jedna z antylop uciekla przed walka!");

		if (teoretyczna[1] - 1 >= 0 && getSwiat()->sprawdzPole(teoretyczna[0], teoretyczna[1] - 1) == ' ') {
			getSwiat()->edytujPlansze(getPolozenie(0), getPolozenie(1), ' ');
			getSwiat()->edytujPlansze(teoretyczna[0], teoretyczna[1] - 1, this->getZnak());
			getSwiat()->changePositionOrganizm(getPolozenie(0), getPolozenie(1), teoretyczna[0], teoretyczna[1] - 1, organizmy);
		}

		else if (teoretyczna[1] + 1 < getSwiat()->getRozmiarY() && getSwiat()->sprawdzPole(teoretyczna[0], teoretyczna[1] + 1) == ' ') {
			getSwiat()->edytujPlansze(getPolozenie(0), getPolozenie(1), ' ');
			getSwiat()->edytujPlansze(teoretyczna[0], teoretyczna[1] + 1, this->getZnak());
			getSwiat()->changePositionOrganizm(getPolozenie(0), getPolozenie(1), teoretyczna[0], teoretyczna[1] + 1, organizmy);
		}

		else if (teoretyczna[0] - 1 >= 0 && getSwiat()->sprawdzPole(teoretyczna[0] - 1, teoretyczna[1]) == ' ') {
			getSwiat()->edytujPlansze(getPolozenie(0), getPolozenie(1), ' ');
			getSwiat()->edytujPlansze(teoretyczna[0] - 1, teoretyczna[1], this->getZnak());
			getSwiat()->changePositionOrganizm(getPolozenie(0), getPolozenie(1), teoretyczna[0] - 1, teoretyczna[1], organizmy);
		}

		else if (teoretyczna[0] + 1 < getSwiat()->getRozmiarX() && getSwiat()->sprawdzPole(teoretyczna[0] + 1, teoretyczna[1] - 1) == ' ') {
			getSwiat()->edytujPlansze(getPolozenie(0), getPolozenie(1), ' ');
			getSwiat()->edytujPlansze(teoretyczna[0] + 1, teoretyczna[1], this->getZnak());
			getSwiat()->changePositionOrganizm(getPolozenie(0) + 1, getPolozenie(1), teoretyczna[0], teoretyczna[1], organizmy);
		}

		return 1;

	}

	return 0;

}

Antylopa::~Antylopa()
{
}