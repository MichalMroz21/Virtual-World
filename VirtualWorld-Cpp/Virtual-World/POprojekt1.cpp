#include <iostream>
#include <vector>
#include <string>
#include <conio.h>
#include <stdlib.h>
#include "GameManager.h"
#include "Swiat.h"
#include "Zwierze.h"
#include "Roslina.h"
#include "Wilk.h"
#include "Owca.h"
#include "Zolw.h"
#include "Lis.h"
#include "Antylopa.h"
#include "Trawa.h"
#include "Mlecz.h"
#include "Guarana.h"
#include "Jagody.h"
#include "Barszcz.h"
#include "Czlowiek.h"
#include "Windows.h"


#define CREDITS_HEIGHT 3

int main()
{
	unsigned int x{}, y{};

	std::cout << "Podaj rozmiar planszy (x)" << std::endl;
	std::cin >> x;
	std::cout << "Podaj rozmiar planszy (y)" << std::endl;
	std::cin >> y;

	int turaUmiejetnosc{ -5 };

	std::vector<std::string> credits{ CREDITS_HEIGHT, std::string(x + 1, ' ') };

	for (auto& i : credits[0]) i = '-';
	credits[0][x] = '\n';

	for (auto& i : credits[2]) i = '-';
	credits[2][x] = '\n';

	credits[1] = "Michal Mroz\n";

	Swiat* swiat = new Swiat({ x,y }, std::vector<std::string> {y, std::string(x, ' ') }, credits);

	std::vector< std::vector<Organizm* > > organizmy{ {} };

	for (int i = 0; i < y; i++) {
		organizmy.push_back({});
	}

	unsigned int cPosY{ y / 2 }, cPosX{ x / 2 };
	
	for (unsigned int i = 0; i < y; i++) {

		for (unsigned int j = 0; j < x; j++) {

			if (i == cPosY && j == cPosX) {
				Organizm* czlowiek = new Czlowiek(swiat, std::vector<unsigned int>{j, i}); organizmy[i].push_back(czlowiek);
				continue;
			}

			swiat->partitionOrganizm(i, j, organizmy);
		}

	}

	bool flag = 1;

	while (flag) {

		system("cls");

		swiat->rysujSwiat();

		int czyCzlowiekIstnieje{};

		if (swiat->findOrganizmByChar(CZLOWIEK, organizmy)) {
			swiat->findOrganizmByChar(CZLOWIEK, organizmy)->podajKierunekRuchu();
			swiat->findOrganizmByChar(CZLOWIEK, organizmy)->podajInfoTarcza(turaUmiejetnosc);
			czyCzlowiekIstnieje = 1;
		}

		else {
			std::cout << "Czlowiek nie zyje!" << std::endl;
			czyCzlowiekIstnieje = 0;
		}

		char ch{};

		ch = _getch();

		switch (ch) {

			case 't': {

				if (czyCzlowiekIstnieje) {

					if (swiat->findOrganizmByChar(CZLOWIEK, organizmy)->getKierunekRuchu() == 0) {
						std::cout << "Podaj strzalkami kierunek ruchu czlowieka przed rozpoczeciem tury!" << std::endl;
						Sleep(1000);
						break;
					}

					else {
						swiat->wykonajTure(swiat, x, y, organizmy);

						if (turaUmiejetnosc != -5) turaUmiejetnosc--;

						if (czyCzlowiekIstnieje && turaUmiejetnosc == 0) {
							swiat->findOrganizmByChar(CZLOWIEK, organizmy)->zmienStanTarczyAldura(0);
						}
						break;
					}
				}

				else {

					swiat->wykonajTure(swiat, x, y, organizmy);

					if (turaUmiejetnosc != -5) turaUmiejetnosc--;

					if (czyCzlowiekIstnieje && turaUmiejetnosc == 0) {
						swiat->findOrganizmByChar(CZLOWIEK, organizmy)->zmienStanTarczyAldura(0);
					}
					break;

				}

			}

			case 'e':
				flag = 0;
				break;

			case KEY_UP:
				if (czyCzlowiekIstnieje) {
					swiat->findOrganizmByChar(CZLOWIEK, organizmy)->zmienKierunekRuchu(1);
				}
				break;

			case KEY_DOWN:
				if (czyCzlowiekIstnieje) {
					swiat->findOrganizmByChar(CZLOWIEK, organizmy)->zmienKierunekRuchu(2);
				}
				break;

			case KEY_LEFT:
				if (czyCzlowiekIstnieje) {
					swiat->findOrganizmByChar(CZLOWIEK, organizmy)->zmienKierunekRuchu(3);
				}
				break;

			case KEY_RIGHT:
				if (czyCzlowiekIstnieje) {
					swiat->findOrganizmByChar(CZLOWIEK, organizmy)->zmienKierunekRuchu(4);
				}
				break;

			case 'u':
				if (czyCzlowiekIstnieje && turaUmiejetnosc == -5) {
					swiat->findOrganizmByChar(CZLOWIEK, organizmy)->zmienStanTarczyAldura(1);
					turaUmiejetnosc = 5;
				}
				else if(czyCzlowiekIstnieje){
					std::cout << " Umiejetnosc ma cooldown lub jest juz aktywowana!" << std::endl;
					Sleep(500);
				}
				break;
		}

	}


	

}

