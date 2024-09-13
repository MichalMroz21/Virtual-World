import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.util.concurrent.TimeUnit;

public class Swiat {

	private ArrayList<Integer> rozmiar;
	private int obecnaTura;
	private ArrayList<StringBuffer> credits;
	private ArrayList<StringBuffer> plansza;
	private StringBuffer Log;
	private int turaUmiejetnosc;
	private Boolean buttonWait;
	private Boolean isSave;
	private Boolean isHex;
	
	public Boolean getIsHex() {
		return isHex;
	}
	
	public void setIsHex(Boolean b) {
		isHex = b;
	}
	
	public int getObecnaTura() {
		return obecnaTura;
	}
	
	public Boolean getIsSave() {
		return isSave;
	}
	
	public void changeIsSave(Boolean b) {
		isSave = b;
	}
	
	public Boolean getButtonWait() {
		return buttonWait;
	}
	
	public void changeButtonWait(Boolean b) {
		buttonWait = b;
	}
	
	public int getTuraUmiejetnosc() {
		return turaUmiejetnosc;
	}
	
	public void changeTuraUmiejetnosc(int i) {
		turaUmiejetnosc = i;
	}
	
	ArrayList<StringBuffer> getPlansza(){
		return plansza;
	}
	
	public void changePlansza(ArrayList<StringBuffer> planszaNew) {
		plansza = planszaNew;
	}
	
	public void changeCredits(ArrayList<StringBuffer> creditsNew) {
		credits = creditsNew;
	}
	
	public void changeObecnaTura(int i) {
		obecnaTura = i;
	}
	
	public void changeRozmiarX(int x) {
		rozmiar.set(0, x);
	}
	
	public void changeRozmiarY(int y) {
		rozmiar.set(1, y);
	}
	
	public void wykonajTure(Swiat swiat, int x, int y, ArrayList<ArrayList<Organizm>> organizmy) throws InterruptedException {
		obecnaTura++;
		
		ArrayList<Organizm> List = new ArrayList<Organizm>();
		
		ArrayList<Integer> byInicjatywa = new ArrayList<Integer>();
		
		for(int Y=0; Y < organizmy.size(); Y++) {
			for(int X=0; X < organizmy.get(Y).size(); X++) {
				List.add(organizmy.get(Y).get(X));
				byInicjatywa.add(organizmy.get(Y).get(X).getInicjatywa());
			}
		}
		
		ArrayList<Organizm> sortedList = new ArrayList<Organizm>();
		
		int max = 0;
		
		while(byInicjatywa.size() > 0) {
			max = byInicjatywa.get(0);
			int j = 0;
			
			for(int i=0; i < byInicjatywa.size(); i++) {
				if(byInicjatywa.get(i) > max) {
					max = byInicjatywa.get(i);
					j = i;
				}
			}
			
			sortedList.add(List.get(j));
			List.remove(j);
			byInicjatywa.remove(j);
		}
		
		int p = 0;
		if(sortedList.size() > 0) p = sortedList.get(0).getInicjatywa();
		
		int pocz = 0;
		
		for(int i = 1; i < sortedList.size(); i++) {
			if(p != sortedList.get(i).getInicjatywa()) {
				Collections.sort(sortedList.subList(pocz, i), new MyComparator());
				pocz = i;
			}
			
			else {
				p = sortedList.get(i).getInicjatywa();
			}
		}
		
		ArrayList<Integer> blackList = new ArrayList<Integer>();
		
		for(int i=0; i < sortedList.size(); i++) {
			Boolean flag = true;
			
			for(int j=0; j < blackList.size(); j++) {
				if(blackList.get(j) == i) flag = false;
			}
			
			if (flag == false) continue;
			
			else {
				sortedList.get(i).akcja(blackList, sortedList, organizmy);
				for (int U = 0; U < 50; ++U) System.out.println();
				swiat.rysujSwiat();
				//TimeUnit.SECONDS.sleep(1);
				for (int U = 0; U < 50; ++U) System.out.println();
			}
			
			}
		
		for(int i=0; i < organizmy.size(); i++) {
			
			for(int j=0; j < organizmy.get(i).size(); j++) {
				organizmy.get(i).get(j).addOneToWiek();
			}
			
		}
		
		swiat.clearLog();
 	}
	
	
	
	public void addToLog(String str) {
		Log.append(str);
		Log.append('\n');
	}
	
	public void clearLog() {
		Log.delete(0, Log.length());
	}
	
	
	
	public void rysujSwiat() {
		for(int i=0; i<credits.size(); i++) {
			for(int j=0; j < credits.get(i).length(); j++) {
				System.out.print(credits.get(i).charAt(j));
			}
		}
		
		for(int i=0; i<plansza.size(); i++) {
			for(int j=0; j < plansza.get(i).length(); j++) {
				System.out.print(plansza.get(i).charAt(j));
			}
			System.out.println(' ');
		}
		
		System.out.println(' ');
		System.out.println("Obecna tura: " + obecnaTura);
		System.out.println("Nastepna tura (t)");
		System.out.println("Wyjscie (e)");
		System.out.println("Zapisz stan gry (z)");
		System.out.println("Zaladuj stan gry (l)");
		
		System.out.println(Log);
	}
	
	
	public void edytujPlansze(int x, int y, String c) { //x 6 //y 5
		if(x < 0 || y < 0 || x >= this.getRozmiarX() || y >= this.getRozmiarY()) return;
		plansza.get(y).replace(x, x + 1, c);
	}
	
	public char sprawdzPole(int x, int y) {
		if(x < 0 || y < 0 || x >= this.getRozmiarX() || y >= this.getRozmiarY()) return '\0';
		else return plansza.get(y).charAt(x);
	}
	
	public int getRozmiarX() {
		return rozmiar.get(0);
	}
	
	public int getRozmiarY() {
		return rozmiar.get(1);
	}
	
	
	
	public Swiat(ArrayList<Integer> rozm, ArrayList<StringBuffer> plansz, ArrayList<StringBuffer> cred){
		this.rozmiar = rozm;
		this.obecnaTura = 0;
		this.plansza = plansz;
		this.credits = cred;
		this.Log = new StringBuffer();
		this.turaUmiejetnosc = -5;
		this.buttonWait = true;
		this.isSave = false;
	}
	
	
	public void makeMove(ArrayList<Integer> polozenie, ArrayList<Integer> teoretyczna, Swiat swiat, int zasieg, int kierunek) {
		ArrayList<Boolean> flags = new ArrayList<Boolean>();
		flags.add(false); flags.add(false); flags.add(false); flags.add(false);
		
		if(polozenie.get(1) - zasieg < 0) {
			flags.set(0, true);
		}
		
		if(polozenie.get(1) + zasieg >= this.getRozmiarY()) {
			flags.set(1, true);
		}
		
		if(polozenie.get(0) - zasieg < 0) {
			flags.set(2, true);
		}
		
		if(polozenie.get(0) + zasieg >= this.getRozmiarX()) {
			flags.set(3, true);
		}
		
		int r = 0;
		
		if(kierunek == 0) {
			
			do {
				Random rand = new Random();
				r = rand.nextInt(4);
			} while(flags.get(r));
		}
		
		else {
			
			r = kierunek - 1;
			
			if(flags.get(r)) {
				teoretyczna.set(0, -1);
				teoretyczna.set(1, -1);
				return;
			}
			
		}
		
		if(r == 0) {
			teoretyczna.set(1, polozenie.get(1) - zasieg);
			teoretyczna.set(0, polozenie.get(0));
		}
		
		if(r == 1) {
			teoretyczna.set(1, polozenie.get(1) + zasieg);
			teoretyczna.set(0, polozenie.get(0));
		}
		
		if(r == 2) {
			teoretyczna.set(0, polozenie.get(0) - zasieg);
			teoretyczna.set(1, polozenie.get(1));
		}
		
		if(r == 3) {
			teoretyczna.set(0, polozenie.get(0) + zasieg);
			teoretyczna.set(1, polozenie.get(1));
		}
		
	}
	
	public void changePositionOrganizm(int x, int y, int newX, int newY, ArrayList<ArrayList<Organizm>> organizmy) {
		
		for(int i=0; i < organizmy.size(); i++) {
			for(int j=0; j < organizmy.get(i).size(); j++) {
				if(organizmy.get(i).get(j).getPolozenie(0) == x && organizmy.get(i).get(j).getPolozenie(1) == y) {
					organizmy.get(i).get(j).changePolozenie(newX, newY);
				}
			}
		}
		
	}
	
	public Boolean dodajPoRozmnozeniu(ArrayList<ArrayList<Organizm>>organizmy, Organizm uderzajacy, Organizm uderzony, int x, int y, Swiat swiat) {
		
		String s = "" + uderzajacy.getZnak();
		swiat.edytujPlansze(x, y, s);
		
		swiat.addOrganizmByXY(x, y, organizmy, uderzajacy.getZnak());
		
		String str = "Przywitajmy nowe zwierze! (" + s + ")";
		swiat.addToLog(str);
		
		return false;
		
	}
	
	public void addOrganizmByXY(int x, int y, ArrayList<ArrayList<Organizm>> organizmy, char c) {
		
		ArrayList<Integer> tempL = new ArrayList<Integer>();
		tempL.add(x); tempL.add(y);
		
		deleteOrganizmByXY(x, y, organizmy);
		
		if(c == 'W') {
			Organizm temp = new Wilk(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'O') {
			Organizm temp = new Owca(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'L') {
			Organizm temp = new Lis(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'Z') {
			Organizm temp = new Zolw(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'A') {
			Organizm temp = new Antylopa(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'C') {
			Organizm temp = new Czlowiek(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'M') {
			Organizm temp = new Mlecz(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'T') {
			Organizm temp = new Trawa(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'G') {
			Organizm temp = new Guarana(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'J') {
			Organizm temp = new Jagody(this, tempL);
			organizmy.get(y).add(temp);
		}
		
		if(c == 'B') {
			Organizm temp = new Barszcz(this, tempL);
			organizmy.get(y).add(temp);
		}
	}
	
	public void rozmnazanie(ArrayList<ArrayList<Organizm>> organizmy, Organizm uderzajacy, Organizm uderzony) {
		
		int y1 = uderzajacy.getPolozenie(1);
		int y2 = uderzony.getPolozenie(1);
		
		int x1 = uderzajacy.getPolozenie(0);
		int x2 = uderzony.getPolozenie(0);
		
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
	
	public Organizm findOrganizmByChar(char c, ArrayList<ArrayList<Organizm>> organizmy) {
		for(int y = 0; y < organizmy.size(); y++) {
			for(int x = 0; x < organizmy.get(y).size(); x++) {
				if(organizmy.get(y).get(x).getZnak() == c) return organizmy.get(y).get(x);
			}
		}
		return organizmy.get(0).get(0);
	}
	
	public Organizm findOrganizmByXY(int posX, int posY, ArrayList<ArrayList<Organizm>> organizmy){
		
		for(int y=0; y < organizmy.size(); y++) {
			for(int x=0; x < organizmy.get(y).size(); x++) {
				if(organizmy.get(y).get(x).getPolozenie(0) == posX && organizmy.get(y).get(x).getPolozenie(1) == posY) return organizmy.get(y).get(x);
			}
		}
		return organizmy.get(0).get(0);
	}
	
	public void deleteOrganizmByXY(int posX, int posY, ArrayList<ArrayList<Organizm>> organizmy) {
		for(int y = 0; y < organizmy.size(); y++) {
			for(int x = 0; x < organizmy.get(y).size(); x++) {
				if(organizmy.get(y).get(x).getPolozenie(0) == posX && organizmy.get(y).get(x).getPolozenie(1) == posY) organizmy.get(y).remove(x);
			}
		}
	}
	
	public void zmienSileByXY(int posX, int posY, ArrayList<ArrayList<Organizm>> organizmy, int zmiana) {
		for(int y=0; y < organizmy.size(); y++) {
			for(int x=0; x < organizmy.get(y).size(); x++) {
				if(organizmy.get(y).get(x).getPolozenie(0) == posX && organizmy.get(y).get(x).getPolozenie(1) == posY) organizmy.get(y).get(x).zmienSile(organizmy.get(y).get(x).getSila() + zmiana);
			}
		}
	}
	
	public void partitionOrganizm(int i, int j, ArrayList<ArrayList<Organizm>> organizmy) {
		
		int r = 0;
		Random rand = new Random();
		r = rand.nextInt(50) + 1;
		
		ArrayList<Integer> tempL = new ArrayList<Integer>();
		tempL.add(j); tempL.add(i);
		
		if(r <= 30) return;
		
		else if(r <= 32) {
			Organizm wilk = new Wilk(this, tempL);
			organizmy.get(i).add(wilk);
		}
		
		else if(r <= 34) {
			Organizm owca = new Owca(this, tempL);
			organizmy.get(i).add(owca);
		}
		
		else if(r <= 36) {
			Organizm lis = new Lis(this, tempL);
			organizmy.get(i).add(lis);
		}
		
		else if(r <= 38) {
			Organizm zolw = new Zolw(this, tempL);
			organizmy.get(i).add(zolw);
		}
		
		else if(r <= 40) {
			Organizm antylopa = new Antylopa(this, tempL);
			organizmy.get(i).add(antylopa);
		}
		
		else if(r <= 42) {
			Organizm mlecz = new Mlecz(this, tempL);
			organizmy.get(i).add(mlecz);
		}
		
		else if(r <= 44) {
			Organizm trawa = new Trawa(this, tempL);
			organizmy.get(i).add(trawa);
		}
		
		else if(r <= 46) {
			Organizm guarana = new Guarana(this, tempL);
			organizmy.get(i).add(guarana);
		}
		
		else if(r <= 48) {
			Organizm jagody = new Jagody(this, tempL);
			organizmy.get(i).add(jagody);
		}
		
		else if(r <= 50) {
			Organizm barszcz = new Barszcz(this, tempL);
			organizmy.get(i).add(barszcz);
		}
		
	}
	
	
	public void usunWokol(int x, int y, ArrayList<ArrayList<Organizm>> organizmy, Organizm uderzajacy) {
		int licznik = 0;
		
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

		String str = "(" + uderzajacy.getZnak() + ") zabil wokol siebie " + Integer.toString(licznik) + " zwierzat";

		addToLog(str);
	}
	
	public Boolean findAndDelete(int x, int y, ArrayList<ArrayList<Organizm>> organizmy, Swiat swiat) {
	
		if(swiat.findOrganizmByXY(x, y, organizmy) != organizmy.get(0).get(0)) {
			if(!swiat.findOrganizmByXY(x, y, organizmy).isPlant()) {
				swiat.edytujPlansze(x, y, " ");
				swiat.deleteOrganizmByXY(x, y, organizmy);
				return true;
			}
		}
		return false;
	}
	
}



