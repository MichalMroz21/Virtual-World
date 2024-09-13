#include "Owca.h"
#include "Zwierze.h"
#include <iostream>
#include "Organizm.h"
#include "Czlowiek.h"

Czlowiek::Czlowiek()
{
	this->kierunekRuchu = 0;
	this->tarczaAldura = 0;
	changeWiek(0);
	changeInicjatywa(4);
	zmienSile(5);
}

Czlowiek::Czlowiek(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeWiek(wiek);
	changeInicjatywa(inicj);
	this->kierunekRuchu = 0;
	this->tarczaAldura = 0;

	getSwiat()->edytujPlansze(poz[0], poz[1], CZLOWIEK);
}

Czlowiek::Czlowiek(Swiat* swiat, std::vector<unsigned int> poz)
{
	changeSwiat(swiat);
	changePolozenie(poz[0], poz[1]);
	changeInicjatywa(4);
	zmienSile(5);
	changeWiek(0);
	this->kierunekRuchu = 0;
	this->tarczaAldura = 0;

	getSwiat()->edytujPlansze(poz[0], poz[1], CZLOWIEK);
}

void Czlowiek::rysowanie()
{
	std::cout << CZLOWIEK;
}

char Czlowiek::getZnak()
{
	return CZLOWIEK;
}

int Czlowiek::getKierunekRuchu()
{
	return kierunekRuchu;
}

void Czlowiek::zmienKierunekRuchu(int a)
{
	kierunekRuchu = a;
}

void Czlowiek::podajKierunekRuchu()
{

	std::cout << "Czlowiek bedzie poruszal sie w: ";

	switch (kierunekRuchu) {

		case 0:
			std::cout << "Okresl kierunek ruchu klikajac odpowiednia strzalke na klawiaturze!" << std::endl;
			break;

		case 1:
			std::cout << "gore" << std::endl;
			break;
		
		case 2:
			std::cout << "dol" << std::endl;
			break;

		case 3:
			std::cout << "lewo" << std::endl;
			break;
		
		case 4:
			std::cout << "prawo" << std::endl;
			break;
	}

}

void Czlowiek::podajInfoTarcza(int tura)
{

	if (tarczaAldura) {
		std::cout << "Tarcza aktywowana! Pozostalo tur: " << tura;
	}

	else{

		if (tura == -5) std::cout << "Mozna aktywowac tarcze! Wcisnij (u)";
		else {
			std::cout << "Tarcza ma cooldown! Mozna aktywowac za: " << 5 + tura << " tur!";
		}
	}

}

void Czlowiek::odstraszenieZPola(std::vector<int>& poleAtakujacego, std::vector<int>& poleAtakowanego, std::vector<std::vector<Organizm*>>& organizmy, char odstraszonego)
{

	int flag{ 0 };

	if (poleAtakowanego[1] - 1 >= 0 && getSwiat()->sprawdzPole(poleAtakowanego[0], poleAtakowanego[1] - 1) == ' ') {
		getSwiat()->edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], ' ');
		getSwiat()->edytujPlansze(poleAtakowanego[0], poleAtakowanego[1] - 1, odstraszonego);
		getSwiat()->changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0], poleAtakowanego[1] - 1, organizmy);
		flag = 1;
	}

	else if (poleAtakowanego[1] + 1 < getSwiat()->getRozmiarY() && getSwiat()->sprawdzPole(poleAtakowanego[0], poleAtakowanego[1] + 1) == ' ') {
		getSwiat()->edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], ' ');
		getSwiat()->edytujPlansze(poleAtakowanego[0], poleAtakowanego[1] + 1, odstraszonego);
		getSwiat()->changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0], poleAtakowanego[1] + 1, organizmy);
		flag = 1;
	}

	else if (poleAtakowanego[0] - 1 >= 0 && getSwiat()->sprawdzPole(poleAtakowanego[0] - 1, poleAtakowanego[1]) == ' ') {
		getSwiat()->edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], ' ');
		getSwiat()->edytujPlansze(poleAtakowanego[0] - 1, poleAtakowanego[1], odstraszonego);
		getSwiat()->changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0] - 1, poleAtakowanego[1], organizmy);
		flag = 1;
	}

	else if (poleAtakowanego[0] + 1 < getSwiat()->getRozmiarX() && getSwiat()->sprawdzPole(poleAtakowanego[0] + 1, poleAtakowanego[1] - 1) == ' ') {
		getSwiat()->edytujPlansze(poleAtakujacego[0], poleAtakujacego[1], ' ');
		getSwiat()->edytujPlansze(poleAtakowanego[0] + 1, poleAtakowanego[1], odstraszonego);
		getSwiat()->changePositionOrganizm(poleAtakujacego[0], poleAtakujacego[1], poleAtakowanego[0] + 1, poleAtakowanego[1], organizmy);
		flag = 1;
	}

	if (flag) {

		std::string str{ "Czlowiek odstraszyl zwierze (" + std::string(1, odstraszonego) + ") tarcza Aldura!" };

		getSwiat()->addToLog(str);
	}

	else {

		std::string str{ "Czlowiek odstraszyl zwierze (" + std::string(1, odstraszonego) + ") tarcza Aldura ale zwierze to nie mialo gdzie uciec! " };

		getSwiat()->addToLog(str);
	}

}

void Czlowiek::zmienStanTarczyAldura(bool b)
{
	tarczaAldura = b;
}

bool Czlowiek::czyJestTarczaAldura()
{
	return tarczaAldura;
}

Czlowiek::~Czlowiek()
{
}