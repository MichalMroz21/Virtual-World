import java.util.ArrayList;
import java.util.Random;

public class Roslina extends Organizm {

	public Roslina(){
	}
	
	public Roslina(Organizm org){
		
	}
	
	@Override
	public void akcja(ArrayList<Integer> blackList, ArrayList<Organizm> sortedList, ArrayList<ArrayList<Organizm>> organizmy) {
		
		if (isRadioactive()) {
			getSwiat().usunWokol(getPolozenie(0), getPolozenie(1), organizmy, this);
		}

		for (int i = 0; i < this.iloscRozp(); i++) {

			Random rand = new Random();
			int temp = rand.nextInt(4);

			if (temp == 0) {

				ArrayList<Integer> teoretyczna = new ArrayList<Integer>();
				teoretyczna.add(0); teoretyczna.add(0);
				
				String s = ""+this.getZnak();
				Boolean czySieWykonalo = false;

				if (getPolozenie(1) - 1 >= 0 && getSwiat().sprawdzPole(getPolozenie(0), getPolozenie(1) - 1) == ' ') {
					getSwiat().edytujPlansze(getPolozenie(0), getPolozenie(1) - 1, s);
					getSwiat().addOrganizmByXY(getPolozenie(0), getPolozenie(1) - 1, organizmy, this.getZnak());
					czySieWykonalo = true;
				}

				else if (getPolozenie(1) + 1 < getSwiat().getRozmiarY() && getSwiat().sprawdzPole(getPolozenie(0), getPolozenie(1) + 1) == ' ') {
					getSwiat().edytujPlansze(getPolozenie(0), getPolozenie(1) + 1, s);
					getSwiat().addOrganizmByXY(getPolozenie(0), getPolozenie(1) + 1, organizmy, this.getZnak());
					czySieWykonalo = true;
				}

				else if (getPolozenie(0) - 1 >= 0 && getSwiat().sprawdzPole(getPolozenie(0) - 1, getPolozenie(1)) == ' ') {
					getSwiat().edytujPlansze(getPolozenie(0) - 1, getPolozenie(1), s);
					getSwiat().addOrganizmByXY(getPolozenie(0) - 1, getPolozenie(1), organizmy, this.getZnak());
					czySieWykonalo = true;
				}

				else if (getPolozenie(0) + 1 < getSwiat().getRozmiarX() && getSwiat().sprawdzPole(getPolozenie(0) + 1, getPolozenie(1) - 1) == ' ') {
					getSwiat().edytujPlansze(getPolozenie(0) + 1, getPolozenie(1), s);
					getSwiat().addOrganizmByXY(getPolozenie(0) + 1, getPolozenie(1), organizmy, this.getZnak());
					czySieWykonalo = true;
				}

				if (czySieWykonalo) {

					String str = "Roslina rozprzestrzenila sie! (" + this.getZnak() + ")";

					getSwiat().addToLog(str);
				}

			}

		}
		
	}
	
	@Override
	public void kolizja(ArrayList<Integer> teoretyczna, ArrayList<Integer> blackList, ArrayList<Organizm> sortedList, Organizm uderzony, Organizm uderzajacy, ArrayList<ArrayList<Organizm>> organizmy) {
		
		char lAtakujacego = uderzajacy.getZnak();
		if (czyZabojcza()) {

			getSwiat().edytujPlansze(uderzajacy.getPolozenie(0), uderzajacy.getPolozenie(1), " ");
			getSwiat().deleteOrganizmByXY(uderzajacy.getPolozenie(0), uderzajacy.getPolozenie(1), organizmy);

			getSwiat().edytujPlansze(teoretyczna.get(0), teoretyczna.get(1), " ");
			getSwiat().deleteOrganizmByXY(teoretyczna.get(0), teoretyczna.get(1), organizmy);

			String str = "Zwierze (" + uderzajacy.getZnak() + ") zjadlo " + uderzony.getZnak() + " i nie zyje";

			getSwiat().addToLog(str);
		}

		else {

			getSwiat().edytujPlansze(uderzajacy.getPolozenie(0), uderzajacy.getPolozenie(1), " ");
			String s = ""+lAtakujacego;
			getSwiat().edytujPlansze(teoretyczna.get(0), teoretyczna.get(1), s);

			getSwiat().deleteOrganizmByXY(teoretyczna.get(0), teoretyczna.get(1), organizmy);
			getSwiat().changePositionOrganizm(uderzajacy.getPolozenie(0), uderzajacy.getPolozenie(1), teoretyczna.get(0), teoretyczna.get(1), organizmy);

			getSwiat().zmienSileByXY(uderzajacy.getPolozenie(0), uderzajacy.getPolozenie(1), organizmy, uderzony.dodawanaSilaPoZjedzeniu());

			if (uderzony.dodawanaSilaPoZjedzeniu() > 0) {
				String str = "Atakujacy (" + uderzajacy.getZnak() + ") zwiekszyl se sile o " + Integer.toString(uderzony.dodawanaSilaPoZjedzeniu());

				getSwiat().addToLog(str);
			}

			String str = "Roslina zostala zjedzona! (" + uderzony.getZnak() + ") przez (" + uderzajacy.getZnak() + ")";

			getSwiat().addToLog(str);

		}
		
		for (int j = 0; j < sortedList.size(); j++) {

			if (sortedList.get(j).getPolozenie(0) == uderzajacy.getPolozenie(0) && sortedList.get(j).getPolozenie(1) == uderzajacy.getPolozenie(1))   blackList.add(j);
			if (sortedList.get(j).getPolozenie(0) == teoretyczna.get(0) && sortedList.get(j).getPolozenie(1) == teoretyczna.get(1) && !czyZabojcza() )   blackList.add(j);

		}
		
	}
	
	@Override
	public void rysowanie() {
		System.out.println('R');
	}
	
	@Override
	public char getZnak() {
		return 'R';
	}
	
	@Override
	public Boolean isPlant() {
		return true;
	}
	
	@Override
	public Boolean czyZabojcza()
	{
		return false;
	}

	@Override
	public int dodawanaSilaPoZjedzeniu()
	{
		return 0;
	}

	@Override
	public Boolean isRadioactive()
	{
		return false;
	}

	@Override
	public int iloscRozp()
	{
		return 1;
	}
	
	
}
