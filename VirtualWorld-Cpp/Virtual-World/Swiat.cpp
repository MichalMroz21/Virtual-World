#include <iostream>
#include <Windows.h>
#include "Swiat.h"
#include "Organizm.h"
#include "DEF.h"
#include "Antylopa.h"
#include "Owca.h"
#include "Mlecz.h"
#include "Wilk.h"
#include "Lis.h"
#include "Zolw.h"
#include "Guarana.h"
#include "Trawa.h"
#include "Jagody.h"
#include "Barszcz.h"
#include "Czlowiek.h"
#include <algorithm>

class Organizm;
class Swiat;

void Swiat::wykonajTure(Swiat* swiat, int x, int y, std::vector <std::vector <Organizm*> >& organizmy)
{
	obecnaTura++;

	std::vector<Organizm*> List{};
	std::vector<int> byInicjatywa{};

	for (int y = 0; y < organizmy.size(); y++) {
		for (int x = 0; x < organizmy[y].size(); x++) {
			List.push_back(organizmy[y][x]);
			byInicjatywa.push_back(organizmy[y][x]->inicjatywa);
		}
	}
				
	std::vector<Organizm*> sortedList{};

	int max{};

	while (byInicjatywa.size() > 0) {
		max = byInicjatywa[0];
		int j{};

		for (int i = 0; i < byInicjatywa.size(); i++) {
			if (byInicjatywa[i] > max) {
				max = byInicjatywa[i];
				j = i;
			}
		}

		sortedList.push_back(List[j]);
		List.erase(List.begin() + j);
		byInicjatywa.erase(byInicjatywa.begin() + j);

	}

	int p{sortedList.size() > 0 ? sortedList[0]->inicjatywa : 0};

	int pocz{};

	for (int i = 1; i < sortedList.size(); i++) {
		if (p != sortedList[i]->inicjatywa) {
			std::sort(sortedList.begin() + pocz, sortedList.begin() + i, [](Organizm* a, Organizm* b) {return a->getWiek() > b->getWiek();});
			pocz = i;
		}

		else {
			p = sortedList[i]->inicjatywa;
		}
	}
	
	std::vector<int> blackList{};

	for (int i = 0; i < sortedList.size(); i++) {

		bool flag = 1;

		for (auto j : blackList) {
			if (j == i) flag = 0;
		}

		if (flag == 0) continue;

		else {
			sortedList[i]->akcja(blackList, sortedList, organizmy);
			system("CLS");
			swiat->rysujSwiat();
			Sleep(DELAY);
			system("CLS");
		}

		
	}

	for (int i = 0; i < organizmy.size(); i++) {
		for (int j = 0; j < organizmy[i].size(); j++) {
			organizmy[i][j]->wiek++;
		}
	}
	
	swiat->clearLog();

}

void Swiat::usunWokol(int x, int y, std::vector<std::vector<Organizm*>>& organizmy, Organizm* uderzajacy)
{
	int licznik{};

	if (y - 1 >= 0 && sprawdzPole(x, y - 1) != ' ') {
		if(findAndDelete(x, y - 1, organizmy, this)) licznik++;
	}

	if (y + 1 < getRozmiarY() && sprawdzPole(x, y + 1) != ' ') {
		if (findAndDelete(x, y + 1, organizmy, this)) licznik++;
	}

	if (x + 1 < getRozmiarX() && sprawdzPole(x + 1, y) != ' ') {
		if (findAndDelete(x + 1, y, organizmy, this)) licznik++;
	}

	if (x - 1  >= 0 && sprawdzPole(x - 1, y) != ' ') {
		if (findAndDelete(x - 1, y, organizmy, this)) licznik++;
	}

	if (x - 1 >= 0 && sprawdzPole(x - 1, y + 1) != ' ' && y + 1 < getRozmiarY()) {
		if (findAndDelete(x - 1, y + 1, organizmy, this)) licznik++;
	}

	if (x - 1 >= 0 && sprawdzPole(x - 1, y - 1) != ' ' && y - 1 >= 0) {
		if (findAndDelete(x - 1, y - 1, organizmy, this)) licznik++;
	}

	if (x + 1 < getRozmiarX() && sprawdzPole(x + 1, y + 1) != ' ' && y + 1 < getRozmiarY()) {
		if (findAndDelete(x + 1, y + 1, organizmy, this)) licznik++;
	}

	if (x + 1 < getRozmiarX() && sprawdzPole(x + 1, y - 1) != ' ' && y - 1 >= 0) {
		if (findAndDelete(x + 1, y - 1, organizmy, this)) licznik++;
	}

	std::string str{ "(" + std::string(1, uderzajacy->getZnak()) + ") zabil wokol siebie " + std::to_string(licznik) + " zwierzat" };

	addToLog(str);

}

bool Swiat::findAndDelete(int x, int y, std::vector<std::vector<Organizm*>>& organizmy, Swiat* swiat) {

	if (!swiat->findOrganizmByXY(x, y, organizmy)->isPlant()) {
		swiat->edytujPlansze(x, y, ' ');
		swiat->deleteOrganizmByXY(x, y, organizmy);
		return 1;
	}

	return 0;
}

void Swiat::rozmnazanie(std::vector<std::vector<Organizm*>>& organizmy, Organizm* uderzajacy, Organizm* uderzony)
{

	int y1 = uderzajacy->polozenie[1];
	int y2 = uderzony->polozenie[1];

	int x1 = uderzajacy->polozenie[0];
	int x2 = uderzony->polozenie[0];

	if (y1 - 1 >= 0 && sprawdzPole(x1, y1 - 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1, y1 - 1, this);
	}

	else if (y1 + 1 < getRozmiarY() && sprawdzPole(x1, y1 + 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1, y1 + 1, this);
	}

	else if (x1 - 1 >= 0 && sprawdzPole(x1 - 1, y1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1 - 1, y1, this);
	}

	else if (x1 - 1 >= 0 && y1 + 1 < getRozmiarY() && sprawdzPole(x1 - 1, y1 + 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1 - 1, y1 + 1, this);
	}

	else if (x1 - 1 >= 0 && y1 - 1 >= 0 && sprawdzPole(x1 - 1, y1 - 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1 - 1, y1 - 1, this);
	}

	else if (x2 + 1 < getRozmiarX() && sprawdzPole(x2 + 1, y2) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 + 1, y2, this);
	}

	else if (x2 - 1 >= 0 && sprawdzPole(x2 - 1, y2) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 - 1, y2, this);
	}

	else if (x2 + 1 < getRozmiarX() && y2 + 1 < getRozmiarY() && sprawdzPole(x2 + 1, y2 + 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 + 1, y2 + 1, this);
	}

	else if (x2 + 1 < getRozmiarX() && y2 - 1 >= 0 && sprawdzPole(x2 + 1, y2 - 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 + 1, y2 - 1, this);
	}

	else if (y2 + 1 < getRozmiarY() && sprawdzPole(x2, y2 + 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2, y2 + 1, this);
	}

	else if (y2 + 1 < getRozmiarY() && x2 + 1 < getRozmiarX() && sprawdzPole(x2 + 1, y2 + 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 + 1, y2 + 1, this);
	}

	else if (y2 + 1 < getRozmiarY() && x2 - 1 >= 0 && sprawdzPole(x2 - 1, y2 + 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 - 1, y2 + 1, this);
	}

	else if (y2 - 1 < getRozmiarY() && x2 - 1 >= 0 && sprawdzPole(x2 - 1, y2 - 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2 - 1, y2 - 1, this);
	}

	else if (y2 - 1 >= 0 && sprawdzPole(x2, y2 - 1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x2, y2 - 1, this);
	}

	else if (x1 + 1 < getRozmiarX() && sprawdzPole(x1, y1) == ' ') {
		dodajPoRozmnozeniu(organizmy, uderzajacy, uderzony, x1 + 1, y1, this);
	}

}

bool Swiat::dodajPoRozmnozeniu(std::vector<std::vector<Organizm*>>& organizmy, Organizm* uderzajacy, Organizm* uderzony, int x, int y, Swiat* swiat)
{
	swiat->edytujPlansze(x, y, uderzajacy->getZnak());
	swiat->addOrganizmByXY(x, y, organizmy, uderzajacy->getZnak());

	std::string str{ "Przywitajmy nowe zwierze! (" + std::string(1, uderzajacy->getZnak()) + ")" };

	swiat->addToLog(str);

	return 0;
}

void Swiat::makeMove(std::vector<int>& polozenie, std::vector<int>& teoretyczna, Swiat* swiat, int zasieg, int kierunek)
{
	std::vector<bool> flags = { 0,0,0,0 };

	if (polozenie[1] - zasieg < 0) {
		flags[0] = 1;
	}

	if (polozenie[1] + zasieg >= swiat->getRozmiarY()) {
		flags[1] = 1;
	}

	if (polozenie[0] - zasieg < 0) {
		flags[2] = 1;
	}

	if (polozenie[0] + zasieg >= swiat->getRozmiarX()) {
		flags[3] = 1;
	}

	int r{};

	if(kierunek == 0){

		do {

			r = rand() % 4;

		} while (flags[r]);

	}

	else {

		r = kierunek - 1;

		if (flags[r]) {
			teoretyczna[0] = -1;
			teoretyczna[1] = -1;
			return;
		}

	}

	if (r == 0) {

		teoretyczna[1] = polozenie[1] - zasieg;
		teoretyczna[0] = polozenie[0];

	}

	if (r == 1) {

		teoretyczna[1] = polozenie[1] + zasieg;
		teoretyczna[0] = polozenie[0];

	}

	if (r == 2) {

		teoretyczna[0] = polozenie[0] - zasieg;
		teoretyczna[1] = polozenie[1];
	}

	if (r == 3) {

		teoretyczna[0] = polozenie[0] + zasieg;
		teoretyczna[1] = polozenie[1];

	}
}

void Swiat::addToLog(std::string str)
{
	Log += str + '\n';
}

void Swiat::clearLog()
{
	Log = std::string(0, ' ');
}

void Swiat::partitionOrganizm(unsigned int i, unsigned int j, std::vector<std::vector<Organizm*>>& organizmy)
{

	int r = rand() % 50 + 1;

	if (r <= 30) return;

	else if (r <= 32) {
		Organizm* barszcz = new Barszcz(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(barszcz);
	}
	else if (r <= 34) {
		Organizm* jagody = new Jagody(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(jagody);
	}
	else if (r <= 36) {
		Organizm* guarana = new Guarana(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(guarana);
	}
	else if (r <= 38) {
		Organizm* mlecz = new Mlecz(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(mlecz);
	}
	else if (r <= 40) {
		Organizm* trawa = new Trawa(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(trawa);
	}
	else if (r <= 42) {
		Organizm* wilk = new Wilk(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(wilk);
	}
	else if (r <= 44) {
		Organizm* owca = new Owca(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(owca);
	}
	else if (r <= 46) {
		Organizm* zolw = new Zolw(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(zolw);
	}
	else if (r <= 48) {
		Organizm* lis = new Lis(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(lis);
	}
	else if (r <= 50) {
		Organizm* antylopa = new Antylopa(this, std::vector<unsigned int>{j, i}); organizmy[i].push_back(antylopa);
	}

}

void Swiat::rysujSwiat()
{

	for (auto i : credits) {
		for (auto j : i) {
			std::cout << j;
		}
	}

	for (auto i : plansza) {
		for (auto j : i) {

			std::cout << j;

		}
		std::cout << std::endl;
	}

	std::cout << std::endl;

	std::cout << "Obecna tura: " << obecnaTura << '\n';
	std::cout << "Nastepna tura (t)" << '\n';
	std::cout << "Wyjscie (e)" << '\n';

	std::cout << Log;

}

void Swiat::edytujPlansze(unsigned int x, unsigned int y, char c)
{
	if (x < 0 || y < 0 || x >= this->getRozmiarX() || y >= this->getRozmiarY()) return;
	plansza[y][x] = c;
}

char Swiat::sprawdzPole(int x, int y)
{
	if (x < 0 || y < 0 || x >= this->getRozmiarX() || y >= this->getRozmiarY()) return '\0';
	else return plansza[y][x];
}

unsigned int Swiat::getRozmiarX()
{
	return rozmiar[0];
}

unsigned int Swiat::getRozmiarY()
{
	return rozmiar[1];
}

Organizm* Swiat::findOrganizmByXY(int posX, int posY, std::vector<std::vector<Organizm*>>& organizmy){
	for (int y = 0; y < organizmy.size(); y++) {
		for (int x = 0; x < organizmy[y].size(); x++) {
			if (organizmy[y][x]->polozenie[0] == posX && organizmy[y][x]->polozenie[1] == posY) return organizmy[y][x];
		}
	}
}

Organizm* Swiat::findOrganizmByChar(char c, std::vector<std::vector<Organizm*>>& organizmy) {
	for (int y = 0; y < organizmy.size(); y++) {
		for (int x = 0; x < organizmy[y].size(); x++) {
			if (organizmy[y][x]->getZnak() == c) return organizmy[y][x];
		}
	}

	return nullptr;
}

void Swiat::deleteOrganizmByXY(int posX, int posY, std::vector<std::vector<Organizm*>>& organizmy)
{
	for (int y = 0; y < organizmy.size(); y++) {
		for (int x = 0; x < organizmy[y].size(); x++) {
			if (organizmy[y][x]->polozenie[0] == posX && organizmy[y][x]->polozenie[1] == posY) organizmy[y].erase(organizmy[y].begin() + x);
		}
	}
}

void Swiat::zmienSileByXY(int posX, int posY, std::vector<std::vector<Organizm*>>& organizmy, int zmiana) {
	for (int y = 0; y < organizmy.size(); y++) {
		for (int x = 0; x < organizmy[y].size(); x++) {
			if (organizmy[y][x]->polozenie[0] == posX && organizmy[y][x]->polozenie[1] == posY) organizmy[y][x]->zmienSile(organizmy[y][x]->getSila() + zmiana);
		}
	}
}

void Swiat::addOrganizmByXY(unsigned int x, unsigned int y, std::vector<std::vector<Organizm*>>& organizmy, char c)
{
	if (c == CZLOWIEK) {
		Organizm* temp = new Czlowiek(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

	if (c == BARSZCZ) {
		Organizm* temp = new Barszcz(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}
	
	if (c == JAGODY) {
		Organizm* temp = new Jagody(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

	if (c == WILK) {
		Organizm* temp = new Wilk(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

	if (c == OWCA) {
		Organizm* temp = new Owca(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

	if (c == ZOLW) {
		Organizm* temp = new Zolw(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

	if (c == LIS) {
		Organizm* temp = new Lis(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

	if (c == ANTYLOPA) {
		Organizm* temp = new Antylopa(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

	if (c == TRAWA) {
		Organizm* temp = new Trawa(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

	if (c == MLECZ) {
		Organizm* temp = new Mlecz(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

	if (c == GUARANA) {
		Organizm* temp = new Guarana(this, std::vector<unsigned int>{x, y});
		organizmy[y].push_back(temp);
	}

}

void Swiat::changePositionOrganizm(int x, int y, int newX, int newY, std::vector<std::vector<Organizm*>>& organizmy)
{
	for (int i = 0; i < organizmy.size(); i++) {
		for (int j = 0; j < organizmy[i].size(); j++) {
			if (organizmy[i][j]->polozenie[0] == x && organizmy[i][j]->polozenie[1] == y) {
				organizmy[i][j]->polozenie[0] = newX;
				organizmy[i][j]->polozenie[1] = newY;
			}
		}
	}
}


Swiat::Swiat(std::vector<unsigned int> rozm, std::vector<std::string> plansz, std::vector<std::string> cred)
{
	this->rozmiar = rozm;
	this->obecnaTura = 0; 
	this->plansza = plansz;
	this->credits = cred; 
}
