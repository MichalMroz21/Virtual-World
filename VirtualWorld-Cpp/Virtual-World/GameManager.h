#pragma once
#include "Organizm.h"

class Organizm;

class Swiat;

class GameManager {

public:

	void makeMove(std::vector<int>& polozenie, std::vector<int>& teoretyczna, Swiat* swiat, int zasieg);
};