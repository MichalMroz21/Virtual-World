import java.util.ArrayList;

public class Lis extends Zwierze {

	public Lis() {
	}
		
		public Lis(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
			changeSwiat(swiat);
			changePolozenie(poz.get(0), poz.get(1));
			changeWiek(wiek);
			changeInicjatywa(inicj);
			
			String s = ""+'L';
			getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
		}
		
		public Lis(Swiat swiat, ArrayList<Integer> poz) {
			changeSwiat(swiat);
			changePolozenie(poz.get(0), poz.get(1));
			changeInicjatywa(7);
			zmienSile(3);
			changeWiek(0);
			
			String s = ""+'L';
			getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
		}
		
		@Override
		public void rysowanie() {
			System.out.println('L');
		}
		
		@Override
		public char getZnak() {
			return 'L';
		}
		
		@Override
		public Boolean dobryWech(Organizm atakowany) {
			if(atakowany.getSila() > 3) {
				getSwiat().addToLog("Jeden z lisow wyweszyl lepszy organizm!");
				return true;
			}
			else return false;
		}
	
}
