#include "Organizm.h"


int Organizm::getInicjatywa()
{
	return inicjatywa;
}

void Organizm::changeInicjatywa(int i)
{
	inicjatywa = i;
}

void Organizm::changeWiek(int i)
{
	wiek = i;
}

int Organizm::getWiek()
{
	return wiek;
}

int Organizm::getPolozenie(int i)
{
	return polozenie[i];
}

std::vector<int>& Organizm::getPolozenie()
{
	return polozenie;
}

void Organizm::changePolozenie(int x, int y)
{
	polozenie[0] = x;
	polozenie[1] = y;
}

Swiat* Organizm::getSwiat()
{
	return swiat;
}

void Organizm::changeSwiat(Swiat* swiat)
{
	this->swiat = swiat;

}

Organizm::Organizm()
{
	this->polozenie = std::vector<int>{ 0,0 };
}

Organizm::~Organizm()
{
}

void Organizm::akcja(std::vector<int>& blackList, std::vector<Organizm*>& sortedList, std::vector <std::vector <Organizm*> >& organizmy)
{
}

void Organizm::kolizja(std::vector<int> teoretyczna, std::vector<int>& blackList, std::vector<Organizm*>& sortedList, Organizm* uderzony, Organizm* uderzajacy, std::vector <std::vector <Organizm*>>& organizmy)
{
}

void Organizm::rysowanie()
{
}

char Organizm::getZnak()
{
	return 0;
}

bool Organizm::czyOdbito(Organizm* atakujacy)
{
	return false;
}

bool Organizm::zmienPolozenie(Swiat* swiat)
{
	return true;
}

bool Organizm::dobryWech(Organizm* atakowany)
{
	return false;
}

int Organizm::zasieg()
{
	return 1;
}

bool Organizm::isPlant()
{
	return false;
}

int Organizm::iloscRozp()
{
	return 1;
}

bool Organizm::ucieczka(std::vector<int>& teoretyczna, std::vector <std::vector <Organizm*>>& organizmy)
{
	return 0;
}

void Organizm::odstraszenieZPola(std::vector<int>& poleAtakujacego, std::vector<int>& poleAtakowanego, std::vector<std::vector<Organizm*>>& organizmy, char odstraszonego)
{
}

int Organizm::dodawanaSilaPoZjedzeniu()
{
	return 0;
}

bool Organizm::czyZabojcza()
{
	return false;
}

bool Organizm::isRadioactive()
{
	return false;
}

int Organizm::getKierunekRuchu()
{
	return 0;
}

void Organizm::zmienKierunekRuchu(int a)
{
}

void Organizm::podajKierunekRuchu()
{
}

void Organizm::podajInfoTarcza(int tura)
{
}

bool Organizm::czyJestTarczaAldura()
{
	return false;
}

void Organizm::zmienStanTarczyAldura(bool b)
{
}

int Organizm::getSila()
{
	return sila;
}

void Organizm::zmienSile(int s)
{
	sila = s;
}
