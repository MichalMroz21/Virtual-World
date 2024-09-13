
import java.util.ArrayList;


public class Wilk extends Zwierze{
	
	public Wilk() {
		
	}
	
	public Wilk(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeWiek(wiek);
		changeInicjatywa(inicj);
		
		String s = ""+'W';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	public Wilk(Swiat swiat, ArrayList<Integer> poz) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeInicjatywa(5);
		zmienSile(9);
		changeWiek(0);
		
		String s = ""+'W';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	@Override
	public void rysowanie() {
		System.out.println('W');
	}
	
	@Override
	public char getZnak() {
		return 'W';
	}
	
}
