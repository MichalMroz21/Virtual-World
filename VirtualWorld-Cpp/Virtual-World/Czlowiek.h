#pragma once
#include "DEF.h"
#include "Zwierze.h"
#include "Organizm.h"

class Czlowiek : public Zwierze {

private:
	int kierunekRuchu;

	bool tarczaAldura;

public:
	Czlowiek();
	Czlowiek(Swiat* swiat, std::vector<unsigned int> poz, int wiek, int inicj, int moc);
	Czlowiek(Swiat* swiat, std::vector<unsigned int> poz);
	void rysowanie() override;
	char getZnak() override;

	int getKierunekRuchu();
	void zmienKierunekRuchu(int a);

	void podajKierunekRuchu();

	void podajInfoTarcza(int tura);

	void odstraszenieZPola(std::vector<int>& poleAtakujacego, std::vector<int>& poleAtakowanego, std::vector <std::vector <Organizm*>>& organizmy, char odstraszonego);

	void zmienStanTarczyAldura(bool b);

	bool czyJestTarczaAldura();

	~Czlowiek();
};
