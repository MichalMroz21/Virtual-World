import java.util.ArrayList;
import java.util.Random;

public class Antylopa extends Zwierze{
	
	public Antylopa() {
	}
		
		public Antylopa(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
			changeSwiat(swiat);
			changePolozenie(poz.get(0), poz.get(1));
			changeWiek(wiek);
			changeInicjatywa(inicj);
			
			String s = ""+'A';
			getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
		}
		
		public Antylopa(Swiat swiat, ArrayList<Integer> poz) {
			changeSwiat(swiat);
			changePolozenie(poz.get(0), poz.get(1));
			changeInicjatywa(4);
			zmienSile(4);
			changeWiek(0);
			
			String s = ""+'A';
			getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
		}
		
		@Override
		public void rysowanie() {
			System.out.println('A');
		}
		
		@Override
		public char getZnak() {
			return 'A';
		}
		
		@Override
		public int zasieg() {
			return 2;
		}
		
		@Override
		public Boolean ucieczka(ArrayList<Integer> teoretyczna, ArrayList<ArrayList<Organizm>> organizmy) {
			Random rand = new Random();
			int temp = rand.nextInt(2);
			
			String s = ""+this.getZnak();
			
			if (temp >= 1) {
				getSwiat().addToLog("Jedna z antylop uciekla przed walka!");

				if (teoretyczna.get(1) - 1 >= 0 && getSwiat().sprawdzPole(teoretyczna.get(0), teoretyczna.get(1) - 1) == ' ') {
					getSwiat().edytujPlansze(getPolozenie(0), getPolozenie(1), " ");
					getSwiat().edytujPlansze(teoretyczna.get(0), teoretyczna.get(1) - 1, s);
					getSwiat().changePositionOrganizm(getPolozenie(0), getPolozenie(1), teoretyczna.get(0), teoretyczna.get(1) - 1, organizmy);
				}

				else if (teoretyczna.get(1) + 1 < getSwiat().getRozmiarY() && getSwiat().sprawdzPole(teoretyczna.get(0), teoretyczna.get(1) + 1) == ' ') {
					getSwiat().edytujPlansze(getPolozenie(0), getPolozenie(1), " ");
					getSwiat().edytujPlansze(teoretyczna.get(0), teoretyczna.get(1) + 1, s);
					getSwiat().changePositionOrganizm(getPolozenie(0), getPolozenie(1), teoretyczna.get(0), teoretyczna.get(1) + 1, organizmy);
				}

				else if (teoretyczna.get(0) - 1 >= 0 && getSwiat().sprawdzPole(teoretyczna.get(0) - 1, teoretyczna.get(1)) == ' ') {
					getSwiat().edytujPlansze(getPolozenie(0), getPolozenie(1), " ");
					getSwiat().edytujPlansze(teoretyczna.get(0) - 1, teoretyczna.get(1), s);
					getSwiat().changePositionOrganizm(getPolozenie(0), getPolozenie(1), teoretyczna.get(0) - 1, teoretyczna.get(1), organizmy);
				}

				else if (teoretyczna.get(0) + 1 < getSwiat().getRozmiarX() && getSwiat().sprawdzPole(teoretyczna.get(0) + 1, teoretyczna.get(1) - 1) == ' ') {
					getSwiat().edytujPlansze(getPolozenie(0), getPolozenie(1), " ");
					getSwiat().edytujPlansze(teoretyczna.get(0) + 1, teoretyczna.get(1), s);
					getSwiat().changePositionOrganizm(getPolozenie(0) + 1, getPolozenie(1), teoretyczna.get(0), teoretyczna.get(1), organizmy);
				}

				return true;

			}

			return false;
		}
	
}
