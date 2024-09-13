import java.util.ArrayList;
import java.util.Random;

public class Zolw extends Zwierze{

	public Zolw(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeWiek(wiek);
		changeInicjatywa(inicj);
		
		String s = ""+'Z';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	public Zolw(Swiat swiat, ArrayList<Integer> poz) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeInicjatywa(1);
		zmienSile(2);
		changeWiek(0);
		
		String s = ""+'Z';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	@Override
	public void rysowanie() {
		System.out.println('Z');
	}
	
	@Override
	public char getZnak() {
		return 'Z';
	}
	
	@Override
	public Boolean czyOdbito(Organizm atakujacy) {
		if(atakujacy.getSila() < 5) {
			getSwiat().addToLog("Jeden zolwi odbil obrazenia!");
			return true;
		}
		else return false;
	}
	
	@Override
	public Boolean zmienPolozenie(Swiat swiat) {
		Random rand = new Random();
		int temp = rand.nextInt(4);
		
		if(temp <= 2) {
			swiat.addToLog("Jeden z zolwi nie ruszyl sie!");
			return false;
		}
		else return true;
	}
	
	
}
