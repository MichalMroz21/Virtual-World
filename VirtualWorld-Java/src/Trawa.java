
import java.util.ArrayList;


public class Trawa extends Roslina{
	
	public Trawa() {
		
	}
	
	public Trawa(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeWiek(wiek);
		changeInicjatywa(inicj);
		
		String s = ""+'T';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	public Trawa(Swiat swiat, ArrayList<Integer> poz) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeInicjatywa(0);
		zmienSile(0);
		changeWiek(0);
		
		String s = ""+'T';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	@Override
	public void rysowanie() {
		System.out.println('T');
	}
	
	@Override
	public char getZnak() {
		return 'T';
	}
	
}
