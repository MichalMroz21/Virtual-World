import java.util.ArrayList;

public class Owca extends Zwierze{

public Owca() {
}
	
	public Owca(Swiat swiat, ArrayList<Integer> poz, int wiek, int inicj, int moc) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeWiek(wiek);
		changeInicjatywa(inicj);
		
		String s = ""+'O';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	public Owca(Swiat swiat, ArrayList<Integer> poz) {
		changeSwiat(swiat);
		changePolozenie(poz.get(0), poz.get(1));
		changeInicjatywa(4);
		zmienSile(4);
		changeWiek(0);
		
		String s = ""+'O';
		getSwiat().edytujPlansze(poz.get(0), poz.get(1), s);
	}
	
	@Override
	public void rysowanie() {
		System.out.println('O');
	}
	
	@Override
	public char getZnak() {
		return 'O';
	}
	
}
