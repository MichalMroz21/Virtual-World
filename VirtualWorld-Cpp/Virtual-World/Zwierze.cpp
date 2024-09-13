#include "Zwierze.h"
#include <iostream>
#include "DEF.h"
#include "Organizm.h"

Zwierze::Zwierze()
{
}

Zwierze::Zwierze(Organizm org)
{
}

void Zwierze::akcja(std::vector<int>& blackList, std::vector<Organizm*>& sortedList, std::vector <std::vector <Organizm*> >& organizmy){

	Organizm* uderzajacy = this;

	if (uderzajacy->zmienPolozenie(getSwiat())) {

		std::vector<int> teoretyczna{ 0,0 };

		getSwiat()->makeMove(getPolozenie(), teoretyczna, getSwiat(), uderzajacy->zasieg(), uderzajacy->getKierunekRuchu());

		if (teoretyczna[0] == -1 && teoretyczna[1] == -1) return;

		if (getSwiat()->sprawdzPole(teoretyczna[0], teoretyczna[1]) == ' ') {

			getSwiat()->edytujPlansze(getPolozenie(0), getPolozenie(1), ' ');
			getSwiat()->edytujPlansze(teoretyczna[0], teoretyczna[1], this->getZnak());

			getSwiat()->changePositionOrganizm(getPolozenie(0), getPolozenie(1), teoretyczna[0], teoretyczna[1], organizmy);

			for (int j = 0; j < sortedList.size(); j++) {

				if (sortedList[j]->getPolozenie(0) == getPolozenie(0) && sortedList[j]->getPolozenie(1) == getPolozenie(1))   blackList.push_back(j);
				if (sortedList[j]->getPolozenie(0) == teoretyczna[0] && sortedList[j]->getPolozenie(1) == teoretyczna[1])   blackList.push_back(j);
				
			}

		}

		else {
			Organizm* uderzony{ getSwiat()->findOrganizmByXY(0, 0, organizmy) };

			uderzony = getSwiat()->findOrganizmByXY(teoretyczna[0], teoretyczna[1], organizmy);
		
			if (uderzony->isPlant()) uderzony->kolizja(teoretyczna, blackList, sortedList, uderzony, uderzajacy, organizmy);
			else kolizja(teoretyczna, blackList, sortedList, uderzony, uderzajacy, organizmy);
		}
	}

}

void Zwierze::kolizja(std::vector<int> teoretyczna, std::vector<int>& blackList, std::vector<Organizm*>& sortedList, Organizm* uderzony, Organizm* uderzajacy, std::vector <std::vector <Organizm*>>& organizmy)
{

	char lAtakujacego = getSwiat()->sprawdzPole(getPolozenie(0), getPolozenie(1));
	char lAtakowanego = getSwiat()->sprawdzPole(teoretyczna[0], teoretyczna[1]);

	int flag{ 1 };

	if (lAtakujacego == lAtakowanego) {
		getSwiat()->rozmnazanie(organizmy, uderzajacy, uderzony);
	}

	else if (!(uderzajacy->ucieczka(teoretyczna, organizmy))) {

		if (!(uderzajacy->dobryWech(uderzony))) {

			if (!(uderzony->czyOdbito(uderzajacy))) {

				if (uderzony->czyJestTarczaAldura()) {
					uderzony->odstraszenieZPola(getPolozenie(), teoretyczna, organizmy, lAtakujacego);
					flag = 0;
				}

				else if (uderzajacy->czyJestTarczaAldura()) {
					uderzajacy->odstraszenieZPola(teoretyczna, getPolozenie(), organizmy, lAtakowanego);
					flag = 0;
				}

				if (flag) {

					if (uderzajacy->getSila() >= uderzony->getSila()) {

						getSwiat()->edytujPlansze(getPolozenie(0), getPolozenie(1), ' ');
						getSwiat()->edytujPlansze(teoretyczna[0], teoretyczna[1], lAtakujacego);

						getSwiat()->deleteOrganizmByXY(teoretyczna[0], teoretyczna[1], organizmy);
						getSwiat()->changePositionOrganizm(getPolozenie(0), getPolozenie(1), teoretyczna[0], teoretyczna[1], organizmy);

						std::string str{ "Organizm (" + std::string(1, uderzony->getZnak()) + ") zabity przez (" + std::string(1, uderzajacy->getZnak()) + ")" };

						getSwiat()->addToLog(str);

					}

					if (uderzajacy->getSila() < uderzony->getSila()) {

						getSwiat()->edytujPlansze(getPolozenie(0), getPolozenie(1), ' ');

						getSwiat()->deleteOrganizmByXY(getPolozenie(0), getPolozenie(1), organizmy);

						std::string str{ "Organizm (" + std::string(1, uderzony->getZnak()) + ") obronil sie przed (" + std::string(1, uderzajacy->getZnak()) + ")" };

						getSwiat()->addToLog(str);

					}

				}

			}
		}

	}

	
	for (int j = 0; j < sortedList.size();  j++) {

		if (sortedList[j]->getPolozenie(0) == getPolozenie(0) && sortedList[j]->getPolozenie(1) == getPolozenie(1))   blackList.push_back(j);
		if (sortedList[j]->getPolozenie(0) == teoretyczna[0] && sortedList[j]->getPolozenie(1) == teoretyczna[1])   blackList.push_back(j);

	}

}

void Zwierze::rysowanie()
{
	std::cout << 'Z';
}

char Zwierze::getZnak()
{
	return 'Z';
}

bool Zwierze::czyOdbito(Organizm* atakujacy)
{
	return false;
}

bool Zwierze::dobryWech(Organizm* atakowany)
{
	return false;
}

bool Zwierze::zmienPolozenie(Swiat* swiat)
{
	return true;
}

bool Zwierze::isPlant()
{
	return false;
}

int Zwierze::zasieg()
{
	return 1;
}

bool Zwierze::ucieczka(std::vector<int>& teoretyczna, std::vector <std::vector <Organizm*>>& organizmy)
{
	return 0;
}

void Zwierze::odstraszenieZPola(std::vector<int>& poleAtakujacego, std::vector<int>& poleAtakowanego, std::vector<std::vector<Organizm*>>& organizmy, char odstraszonego)
{
}

int Zwierze::getKierunekRuchu()
{
	return 0;
}

void Zwierze::zmienKierunekRuchu(int a)
{
}

void Zwierze::podajKierunekRuchu()
{
}

void Zwierze::podajInfoTarcza(int tura)
{
}

void Zwierze::zmienStanTarczyAldura(bool b)
{
}

bool Zwierze::czyJestTarczaAldura()
{
	return false;
}

Zwierze::~Zwierze()
{
}
