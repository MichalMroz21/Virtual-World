#include "Roslina.h"
#include <iostream>

Roslina::Roslina()
{
}

Roslina::Roslina(Organizm org)
{
}

void Roslina::akcja(std::vector<int>& blackList, std::vector<Organizm*>& sortedList, std::vector <std::vector <Organizm*> >& organizmy)
{

	if (isRadioactive()) {
		getSwiat()->usunWokol(getPolozenie(0), getPolozenie(1), organizmy, this);
	}

	for (int i = 0; i < this->iloscRozp(); i++) {

		int temp = rand() % 4;

		if (!temp) {

			Organizm* uderzajacy = this;

			std::vector<int> teoretyczna{ 0,0 };

			bool czySieWykonalo = 0;

			if (getPolozenie(1) - 1 >= 0 && getSwiat()->sprawdzPole(getPolozenie(0), getPolozenie(1) - 1) == ' ') {
				getSwiat()->edytujPlansze(getPolozenie(0), getPolozenie(1) - 1, this->getZnak());
				getSwiat()->addOrganizmByXY(getPolozenie(0), getPolozenie(1) - 1, organizmy, this->getZnak());
				czySieWykonalo = 1;
			}

			else if (getPolozenie(1) + 1 < getSwiat()->getRozmiarY() && getSwiat()->sprawdzPole(getPolozenie(0), getPolozenie(1) + 1) == ' ') {
				getSwiat()->edytujPlansze(getPolozenie(0), getPolozenie(1) + 1, this->getZnak());
				getSwiat()->addOrganizmByXY(getPolozenie(0), getPolozenie(1) + 1, organizmy, this->getZnak());
				czySieWykonalo = 1;
			}

			else if (getPolozenie(0) - 1 >= 0 && getSwiat()->sprawdzPole(getPolozenie(0) - 1, getPolozenie(1)) == ' ') {
				getSwiat()->edytujPlansze(getPolozenie(0) - 1, getPolozenie(1), this->getZnak());
				getSwiat()->addOrganizmByXY(getPolozenie(0) - 1, getPolozenie(1), organizmy, this->getZnak());
				czySieWykonalo = 1;
			}

			else if (getPolozenie(0) + 1 < getSwiat()->getRozmiarX() && getSwiat()->sprawdzPole(getPolozenie(0) + 1, getPolozenie(1) - 1) == ' ') {
				getSwiat()->edytujPlansze(getPolozenie(0) + 1, getPolozenie(1), this->getZnak());
				getSwiat()->addOrganizmByXY(getPolozenie(0) + 1, getPolozenie(1), organizmy, this->getZnak());
				czySieWykonalo = 1;
			}

			if (czySieWykonalo) {

				std::string str{ "Roslina rozprzestrzenila sie! (" + std::string(1, this->getZnak()) + ")" };

				getSwiat()->addToLog(str);
			}

		}

	}

}

void Roslina::kolizja(std::vector<int> teoretyczna, std::vector<int>& blackList, std::vector<Organizm*>& sortedList, Organizm* uderzony, Organizm* uderzajacy, std::vector <std::vector <Organizm*>>& organizmy)
{

	char lAtakujacego = uderzajacy->getZnak();
	char lAtakowanego = getSwiat()->sprawdzPole(teoretyczna[0], teoretyczna[1]);

	if (czyZabojcza()) {

		getSwiat()->edytujPlansze(uderzajacy->getPolozenie(0), uderzajacy->getPolozenie(1), ' ');
		getSwiat()->deleteOrganizmByXY(uderzajacy->getPolozenie(0), uderzajacy->getPolozenie(1), organizmy);

		getSwiat()->edytujPlansze(teoretyczna[0], teoretyczna[1], ' ');
		getSwiat()->deleteOrganizmByXY(teoretyczna[0], teoretyczna[1], organizmy);

		std::string str{ "Zwierze (" + std::string(1, uderzajacy->getZnak()) + ") zjadlo " + std::string(1, uderzony->getZnak()) + " i nie zyje" };

		getSwiat()->addToLog(str);
	}

	else {

		getSwiat()->edytujPlansze(uderzajacy->getPolozenie(0), uderzajacy->getPolozenie(1), ' ');
		getSwiat()->edytujPlansze(teoretyczna[0], teoretyczna[1], lAtakujacego);

		getSwiat()->deleteOrganizmByXY(teoretyczna[0], teoretyczna[1], organizmy);
		getSwiat()->changePositionOrganizm(uderzajacy->getPolozenie(0), uderzajacy->getPolozenie(1), teoretyczna[0], teoretyczna[1], organizmy);

		getSwiat()->zmienSileByXY(uderzajacy->getPolozenie(0), uderzajacy->getPolozenie(1), organizmy, uderzony->dodawanaSilaPoZjedzeniu());

		if (uderzony->dodawanaSilaPoZjedzeniu()) {
			std::string str{ "Atakujacy (" + std::string(1, uderzajacy->getZnak()) + ") zwiekszyl se sile o " + std::to_string(uderzony->dodawanaSilaPoZjedzeniu()) };

			getSwiat()->addToLog(str);
		}

		std::string str{ "Roslina zostala zjedzona! (" + std::string(1, uderzony->getZnak()) + ") przez (" + std::string(1, uderzajacy->getZnak()) + ")" };

		getSwiat()->addToLog(str);

	}
	
	for (int j = 0; j < sortedList.size(); j++) {

		if (sortedList[j]->getPolozenie(0) == uderzajacy->getPolozenie(0) && sortedList[j]->getPolozenie(1) == uderzajacy->getPolozenie(1))   blackList.push_back(j);
		if (sortedList[j]->getPolozenie(0) == teoretyczna[0] && sortedList[j]->getPolozenie(1) == teoretyczna[1] && !czyZabojcza() )   blackList.push_back(j);

	}

}

void Roslina::rysowanie()
{
}

bool Roslina::isPlant()
{
	return 1;
}

char Roslina::getZnak()
{
	return 0;
}

bool Roslina::czyZabojcza()
{
	return false;
}

int Roslina::dodawanaSilaPoZjedzeniu()
{
	return 0;
}

bool Roslina::isRadioactive()
{
	return false;
}

Roslina::~Roslina()
{
}

int Roslina::iloscRozp()
{
	return 1;
}

