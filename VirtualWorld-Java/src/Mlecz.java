
import java.util.ArrayList;


public class Mlecz extends Roslina{
	
	public Mlecz() {
		
	}
	
	public Mlecz(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeWiek(wiek);
		changeInicjatywa(inicj);
		
		String s = ""+'M';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	public Mlecz(Swiat swiat, ArrayList<Integer> poz) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeInicjatywa(0);
		zmienSile(0);
		changeWiek(0);
		
		String s = ""+'M';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	@Override
	public void rysowanie() {
		System.out.println('M');
	}
	
	@Override
	public char getZnak() {
		return 'M';
	}
	
	@Override
	public int iloscRozp() {
		return 3;
	}
	
}
