
import java.util.ArrayList;


public class Barszcz extends Roslina{
	
	public Barszcz() {
		
	}
	
	public Barszcz(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeWiek(wiek);
		changeInicjatywa(inicj);
		
		String s = ""+'B';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	public Barszcz(Swiat swiat, ArrayList<Integer> poz) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeInicjatywa(0);
		zmienSile(10);
		changeWiek(0);
		
		String s = ""+'B';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	@Override
	public void rysowanie() {
		System.out.println('B');
	}
	
	@Override
	public char getZnak() {
		return 'B';
	}
	
	@Override
	public Boolean czyZabojcza() {
		return true;
	}
	
	@Override
	public Boolean isRadioactive() {
		return true;
	}
	
}
