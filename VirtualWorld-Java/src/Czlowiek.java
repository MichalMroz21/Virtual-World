import java.util.ArrayList;

public class Czlowiek extends Zwierze{
	
	private int kierunekRuchu;
	private Boolean tarczaAldura;

	public Czlowiek() {
	}
		
		public Czlowiek(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
			changeSwiat(swiat);
			changePolozenie(poz.get(0), poz.get(1));
			changeWiek(wiek);
			changeInicjatywa(inicj);
			
			this.kierunekRuchu = 0;
			this.tarczaAldura = false;
			
			String s = ""+'C';
			getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
		}
		
		public Czlowiek(Swiat swiat, ArrayList<Integer> poz) {
			changeSwiat(swiat);
			changePolozenie(poz.get(0), poz.get(1));
			changeInicjatywa(4);
			zmienSile(5);
			changeWiek(0);
			
			this.kierunekRuchu = 0;
			this.tarczaAldura = false;
			
			String s = ""+'C';
			getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
		}
		
		@Override
		public void rysowanie() {
			System.out.println('C');
		}
		
		@Override
		public char getZnak() {
			return 'C';
		}
		
		@Override
		public String podajKierunekRuchu() {
			String s = "";
			System.out.print("Czlowiek bedzie poruszal sie w: ");
			s += "Czlowiek bedzie poruszal sie w: ";
			
			switch(kierunekRuchu) {
				case 0:{
					System.out.println("Okresl kierunek ruchu klikajac odpowiednia strzalke na klawiaturze!");
					s += "Okresl kierunek ruchu klikajac odpowiednia strzalke na klawiaturze!";
					break;
				}
				
				case 1:{
					System.out.println("gore");
					s += "gore";
					break;
				}
				
				case 2:{
					System.out.println("dol");
					s += "dol";
					break;
				}
				
				case 3:{
					System.out.println("lewo");
					s += "lewo";
					break;
				}
				
				case 4:{
					System.out.println("prawo");
					s += "prawo";
					break;
				}
				
			}
			return s;
		}
		
		@Override
		public String podajInfoTarcza(int tura) {
			String ret = "";
			if(tarczaAldura) {
				System.out.print("Tarcza aktywowana! Pozostalo tur: " + Integer.toString(tura));
				ret += "Tarcza aktywowana! Pozostalo tur: " + Integer.toString(tura);
			}
			
			else {
				
				if(tura == -5) {
					System.out.print("Mozna aktywowac tarcze!");
					ret += "Mozna aktywowac tarcze!";
				}
				
				else {
					System.out.print("Tarcza ma cooldown! Mozna aktywowac za: " + Integer.toString(5 + tura) + " tur!");
					ret += "Tarcza ma cooldown! Mozna aktywowac za: " + Integer.toString(5 + tura) + " tur!";
				}
			}
			return ret;
		}
		
		@Override
		public void odstraszenieZPola(ArrayList<Integer> poleAtakujacego, ArrayList<Integer> poleAtakowanego, ArrayList<ArrayList<Organizm>> organizmy, char odstraszonego) {
			Boolean flag = false;
			
			String Odstraszonego = ""+odstraszonego;
			
			if (poleAtakowanego.get(1) - 1 >= 0 && getSwiat().sprawdzPole(poleAtakowanego.get(0), poleAtakowanego.get(1) - 1) == ' ') {
				getSwiat().edytujPlansze(poleAtakujacego.get(0), poleAtakujacego.get(1), " ");
				getSwiat().edytujPlansze(poleAtakowanego.get(0), poleAtakowanego.get(1) - 1, Odstraszonego);
				getSwiat().changePositionOrganizm(poleAtakujacego.get(0), poleAtakujacego.get(1), poleAtakowanego.get(0), poleAtakowanego.get(1) - 1, organizmy);
				flag = true;
			}

			else if (poleAtakowanego.get(1) + 1 < getSwiat().getRozmiarY() && getSwiat().sprawdzPole(poleAtakowanego.get(0), poleAtakowanego.get(1) + 1) == ' ') {
				getSwiat().edytujPlansze(poleAtakujacego.get(0), poleAtakujacego.get(1), " ");
				getSwiat().edytujPlansze(poleAtakowanego.get(0), poleAtakowanego.get(1) + 1, Odstraszonego);
				getSwiat().changePositionOrganizm(poleAtakujacego.get(0), poleAtakujacego.get(1), poleAtakowanego.get(0), poleAtakowanego.get(1) + 1, organizmy);
				flag = true;
			}

			else if (poleAtakowanego.get(0) - 1 >= 0 && getSwiat().sprawdzPole(poleAtakowanego.get(0) - 1, poleAtakowanego.get(1)) == ' ') {
				getSwiat().edytujPlansze(poleAtakujacego.get(0), poleAtakujacego.get(1), " ");
				getSwiat().edytujPlansze(poleAtakowanego.get(0) - 1, poleAtakowanego.get(1), Odstraszonego);
				getSwiat().changePositionOrganizm(poleAtakujacego.get(0), poleAtakujacego.get(1), poleAtakowanego.get(0) - 1, poleAtakowanego.get(1), organizmy);
				flag = true;
			}

			else if (poleAtakowanego.get(0) + 1 < getSwiat().getRozmiarX() && getSwiat().sprawdzPole(poleAtakowanego.get(0) + 1, poleAtakowanego.get(1) - 1) == ' ') {
				getSwiat().edytujPlansze(poleAtakujacego.get(0), poleAtakujacego.get(1), " ");
				getSwiat().edytujPlansze(poleAtakowanego.get(0) + 1, poleAtakowanego.get(1), Odstraszonego);
				getSwiat().changePositionOrganizm(poleAtakujacego.get(0), poleAtakujacego.get(1), poleAtakowanego.get(0) + 1, poleAtakowanego.get(1), organizmy);
				flag = true;
			}

			if (flag) {

				String str = "Czlowiek odstraszyl zwierze (" + odstraszonego + ") tarcza Aldura!";

				getSwiat().addToLog(str);
			}

			else {

				String str = "Czlowiek odstraszyl zwierze (" + odstraszonego + ") tarcza Aldura ale zwierze to nie mialo gdzie uciec! ";

				getSwiat().addToLog(str);
			}
		}
		
		@Override
		public void zmienStanTarczyAldura(Boolean b) {
			tarczaAldura = b;
		}
	
		@Override
		public Boolean czyJestTarczaAldura() {
			return tarczaAldura;
		}
		
		@Override
		public void zmienKierunekRuchu(int a) {
			kierunekRuchu = a;
		}
		
		@Override
		public int getKierunekRuchu() {
			return kierunekRuchu;
		}
}
