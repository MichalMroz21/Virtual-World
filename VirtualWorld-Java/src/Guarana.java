
import java.util.ArrayList;


public class Guarana extends Roslina{
	
	public Guarana() {
		
	}
	
	public Guarana(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeWiek(wiek);
		changeInicjatywa(inicj);
		
		String s = ""+'G';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	public Guarana(Swiat swiat, ArrayList<Integer> poz) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeInicjatywa(0);
		zmienSile(0);
		changeWiek(0);
		
		String s = ""+'G';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	@Override
	public void rysowanie() {
		System.out.println('G');
	}
	
	@Override
	public char getZnak() {
		return 'G';
	}
	
	@Override
	public int dodawanaSilaPoZjedzeniu() {
		return 3;
	}
	
}
