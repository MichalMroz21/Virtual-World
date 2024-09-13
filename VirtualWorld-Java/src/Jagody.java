
import java.util.ArrayList;


public class Jagody extends Roslina{
	
	public Jagody() {
		
	}
	
	public Jagody(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeWiek(wiek);
		changeInicjatywa(inicj);
		
		String s = ""+'J';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	public Jagody(Swiat swiat, ArrayList<Integer> poz) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeInicjatywa(0);
		zmienSile(99);
		changeWiek(0);
		
		String s = ""+'J';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	@Override
	public void rysowanie() {
		System.out.println('J');
	}
	
	@Override
	public char getZnak() {
		return 'J';
	}
	
	@Override
	public Boolean czyZabojcza() {
		return true;
	}
	
}
