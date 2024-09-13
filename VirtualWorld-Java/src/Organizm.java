import java.util.ArrayList;

public abstract class Organizm {

private Swiat swiat;
private ArrayList<Integer> polozenie;
private int sila;
private int inicjatywa;
private int wiek;

public int getInicjatywa() {
	return inicjatywa;
}

public void changeInicjatywa(int i) {
	this.inicjatywa = i;
}

public void changeWiek(int i) {
	wiek = i;
}

public int getWiek() {
	return wiek;
}

public void addOneToWiek() {
	wiek++;
}

public int getPolozenie(int i) {
	return polozenie.get(i);
}

public ArrayList<Integer> getPolozenie(){
	return polozenie;
}

public void changePolozenie(int x, int y) {
	polozenie.set(0, x);
	polozenie.set(1, y);
}

public Swiat getSwiat() {
	return swiat;
}

public void changeSwiat(Swiat swiat) {
	this.swiat = swiat;
}

public Organizm(){
	this.polozenie = new ArrayList<Integer>();
	polozenie.add(0);
	polozenie.add(0);
}

public char getZnak() {
	return 0;
}

public Boolean czyOdbito(Organizm atakujacy) {
	return false;
}

public Boolean zmienPolozenie(Swiat swiat) {
	return true;
}

public Boolean dobryWech(Organizm atakowany) {
	return false;
}

public int zasieg() {
	return 1;
}

public Boolean isPlant() {
	return false;
}

public int iloscRozp() {
	return 1;
}

public Boolean ucieczka(ArrayList<Integer> teoretyczna, ArrayList<ArrayList<Organizm>> organizmy) {
	return false;
}

public void odstraszenieZPola(ArrayList<Integer> poleAtakujacego, ArrayList<Integer> poleAtakowanego, ArrayList<ArrayList<Organizm>> organizmy, char odstraszonego) {
	
}

public int dodawanaSilaPoZjedzeniu() {
	return 0;
}

public Boolean czyZabojcza() {
	return false;
}

public Boolean isRadioactive() {
	return false;
}

public int getKierunekRuchu() {
	return 0;
}

public void zmienKierunekRuchu(int a) {
}

public String podajKierunekRuchu() {
	return null;
}

public String podajInfoTarcza(int tura) {
	return null;
}

public Boolean czyJestTarczaAldura() {
	return false;
}

public void zmienStanTarczyAldura(Boolean b) {
}

public int getSila() {
	return sila;
}

public void zmienSile(int s) {
	sila = s;
}

public void rysowanie() {	
}


public void akcja(ArrayList<Integer> blackList, ArrayList<Organizm> sortedList,
		ArrayList<ArrayList<Organizm>> organizmy) {

	
}

public void kolizja(ArrayList<Integer> teoretyczna, ArrayList<Integer> blackList, ArrayList<Organizm> sortedList,
		Organizm uderzony, Organizm uderzajacy, ArrayList<ArrayList<Organizm>> organizmy) {
	
}

	
}
