import java.util.ArrayList;

public class Zwierze extends Organizm {

	public Zwierze(){
	}
	
	public Zwierze(Organizm org){
		
	}
	
	@Override
	public void akcja(ArrayList<Integer> blackList, ArrayList<Organizm> sortedList, ArrayList<ArrayList<Organizm>> organizmy){
		Organizm uderzajacy = this;
		
		if(uderzajacy.zmienPolozenie(this.getSwiat())) {
			
			ArrayList<Integer> teoretyczna = new ArrayList<Integer>();
			teoretyczna.add(0); teoretyczna.add(0);
			
			this.getSwiat().makeMove(this.getPolozenie(), teoretyczna, this.getSwiat(), uderzajacy.zasieg(), uderzajacy.getKierunekRuchu());
			
			if(teoretyczna.get(0) == -1 && teoretyczna.get(1) == -1) return;
			
			if(this.getSwiat().sprawdzPole(teoretyczna.get(0), teoretyczna.get(1)) == ' ') {
				
				this.getSwiat().edytujPlansze(this.getPolozenie(0), this.getPolozenie(1), " ");
				String s = "" + this.getZnak();
				this.getSwiat().edytujPlansze(teoretyczna.get(0), teoretyczna.get(1), s);
				
				this.getSwiat().changePositionOrganizm(this.getPolozenie(0), this.getPolozenie(1), teoretyczna.get(0), teoretyczna.get(1), organizmy);
				
				for(int j=0; j < sortedList.size(); j++) {
					
					if(sortedList.get(j).getPolozenie(0) == this.getPolozenie(0) && sortedList.get(j).getPolozenie(1) == this.getPolozenie(1)) blackList.add(j);
					if(sortedList.get(j).getPolozenie(0) == teoretyczna.get(0) && sortedList.get(j).getPolozenie(1) == teoretyczna.get(1)) blackList.add(j);
					
				}
					
			}
			
			else {
				
				Organizm uderzony = this.getSwiat().findOrganizmByXY(0, 0, organizmy);
				
				uderzony = getSwiat().findOrganizmByXY(teoretyczna.get(0), teoretyczna.get(1), organizmy);
				
				if(uderzony != null) {
					if(uderzony.isPlant()) uderzony.kolizja(teoretyczna, blackList, sortedList, uderzony, uderzajacy, organizmy);
					else this.kolizja(teoretyczna, blackList, sortedList, uderzony, uderzajacy, organizmy);
				}
				
			}
			
		}
		
	}
	
	@Override
	public void kolizja(ArrayList<Integer> teoretyczna, ArrayList<Integer> blackList, ArrayList<Organizm> sortedList, Organizm uderzony, Organizm uderzajacy, ArrayList<ArrayList<Organizm>> organizmy) {
		
		char lAtakujacego = this.getSwiat().sprawdzPole(this.getPolozenie(0), this.getPolozenie(1));
		char lAtakowanego = this.getSwiat().sprawdzPole(teoretyczna.get(0), teoretyczna.get(1));
		
		Boolean flag = true;
		
		if(lAtakujacego == lAtakowanego) {
			this.getSwiat().rozmnazanie(organizmy, uderzajacy, uderzony);
		}
		
		else if(!(uderzajacy.ucieczka(teoretyczna,  organizmy))) {
			
			if(!(uderzajacy.dobryWech(uderzony))) {
				
				if(!(uderzony.czyOdbito(uderzajacy))) {
					
					if(uderzony.czyJestTarczaAldura()) {
						uderzony.odstraszenieZPola(this.getPolozenie(), teoretyczna, organizmy, lAtakujacego);
						flag = false;
					}
					
					else if(uderzajacy.czyJestTarczaAldura()) {
						uderzajacy.odstraszenieZPola(teoretyczna, this.getPolozenie(), organizmy, lAtakowanego);
						flag = false;
					}
					
					if (flag) {

						if (uderzajacy.getSila() >= uderzony.getSila()) {

							this.getSwiat().edytujPlansze(this.getPolozenie(0), this.getPolozenie(1), " ");
							String s = "" + lAtakujacego;
							this.getSwiat().edytujPlansze(teoretyczna.get(0), teoretyczna.get(1), s);

							this.getSwiat().deleteOrganizmByXY(teoretyczna.get(0), teoretyczna.get(1), organizmy);
							this.getSwiat().changePositionOrganizm(this.getPolozenie(0), this.getPolozenie(1), teoretyczna.get(0), teoretyczna.get(1), organizmy);

							String str = "Organizm (" + uderzony.getZnak() + ") zabity przez (" + uderzajacy.getZnak() + ")";

							this.getSwiat().addToLog(str);

						}

						if (uderzajacy.getSila() < uderzony.getSila()) {

							this.getSwiat().edytujPlansze(getPolozenie(0), getPolozenie(1), " ");

							this.getSwiat().deleteOrganizmByXY(getPolozenie(0), getPolozenie(1), organizmy);

							String str = "Organizm (" + uderzony.getZnak() + ") obronil sie przed (" + uderzajacy.getZnak() + ")";

							this.getSwiat().addToLog(str);

						}

					}
				}
				
			}
			
		}
		
		
		for (int j = 0; j < sortedList.size();  j++) {

			if (sortedList.get(j).getPolozenie(0) == this.getPolozenie(0) && sortedList.get(j).getPolozenie(1) == this.getPolozenie(1))   blackList.add(j);
			if (sortedList.get(j).getPolozenie(0) == teoretyczna.get(0) && sortedList.get(j).getPolozenie(1) == teoretyczna.get(1))   blackList.add(j);

		}
		
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
		return false;
	}
	
	@Override
	public Boolean zmienPolozenie(Swiat swiat) {
		return true;
	}
	
	@Override
	public Boolean isPlant() {
		return false;
	}
	
	@Override
	public int zasieg() {
		return 1;
	}
	
	@Override
	public Boolean ucieczka(ArrayList<Integer> teoretyczna, ArrayList<ArrayList<Organizm>> organizmy) {
		return false;
	}
	
	@Override
	public void odstraszenieZPola(ArrayList<Integer> poleAtakujacego, ArrayList<Integer> poleAtakowanego, ArrayList<ArrayList<Organizm>> organizmy, char odstraszonego) {
		
	}	
	
	@Override
	public int getKierunekRuchu() {
		return 0;
	}
	
	public void zmienKierunekRuchu(int a) {
	}
	
	public String podajInfoTarcza(int tura) {
		return null;
	}
	
	public void zmienStanTarczyAldura(Boolean b) {
	}
	
	@Override
	public String podajKierunekRuchu() {
		return null;
	}
	
	@Override
	public Boolean czyJestTarczaAldura() {
		return false;
	}
	
	
	
}
