#pragma once
#include <vector>
#include <string>
#include "Organizm.h"
#include "GameManager.h"


class Organizm;

class Swiat{

private:

	std::vector<unsigned int> rozmiar;

	int obecnaTura;

	std::vector<std::string> credits;

	std::vector<std::string> plansza;

	std::string Log{};

public:

	void wykonajTure(Swiat* swiat, int x, int y, std::vector <std::vector <Organizm*> >& organizmy);

	void usunWokol(int x, int y, std::vector <std::vector <Organizm*> >& organizmy, Organizm* uderzajacy);

	void addToLog(std::string str);

	void clearLog();

	void partitionOrganizm(unsigned int i, unsigned int j, std::vector <std::vector <Organizm*> >& organizmy);

	void rysujSwiat();

	bool findAndDelete(int x, int y, std::vector<std::vector<Organizm*>>& organizmy, Swiat* swiat);

	void rozmnazanie(std::vector <std::vector <Organizm*>>& organizmy, Organizm* uderzajacy, Organizm* uderzony);

	bool dodajPoRozmnozeniu(std::vector <std::vector <Organizm*>>& organizmy, Organizm* uderzajacy, Organizm* uderzony, int x, int y, Swiat* swiat);

	Organizm* findOrganizmByChar(char c, std::vector<std::vector<Organizm*>>& organizmy);

	void edytujPlansze(unsigned int x, unsigned int y, char c);

	char sprawdzPole(int x, int y);

	unsigned int getRozmiarX();

	unsigned int getRozmiarY();

	Organizm* findOrganizmByXY(int x, int y, std::vector< std::vector <Organizm* >>& organizmy);
		
	void deleteOrganizmByXY(int x, int y, std::vector < std::vector <Organizm* >>& organizmy);

	void addOrganizmByXY(unsigned int x, unsigned int y, std::vector < std::vector <Organizm*>>& organizmy, char c);

	void changePositionOrganizm(int x, int y, int newX, int newY, std::vector < std::vector <Organizm*>>& organizmy);

	void zmienSileByXY(int posX, int posY, std::vector<std::vector<Organizm*>>& organizmy, int zmiana);

	void makeMove(std::vector<int>& polozenie, std::vector<int>& teoretyczna, Swiat* swiat, int zasieg, int kierunek);

	Swiat(std::vector<unsigned int> rozm, std::vector<std::string> plansz, std::vector<std::string> cred);




};