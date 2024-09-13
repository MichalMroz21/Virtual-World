import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class Main {

	public static void main(String[] args) throws InterruptedException {
		int x = 0;
		int y = 0;
		
		Boolean isHex;
		
		final int CREDITS_HEIGHT = 3;
		
		GUI gu = new GUI();
		
		gu.setUpStartingGUI();
		
		do {
			Thread.sleep(10);
		} while(gu.getIsStart());
		
		x = gu.getWidth();
		y = gu.getHeight();
		
		isHex = gu.getIsChecked();
			
			ArrayList<StringBuffer> credits = new ArrayList<StringBuffer>();
			for(int i=0; i<CREDITS_HEIGHT; i++) {
				if(!(i % 2 > 0)) {
					char[] chars = new char[x + 1];
					Arrays.fill(chars, '-');
					chars[x] = '\n';
					String s = new String(chars);
					StringBuffer temp = new StringBuffer(s);
					credits.add(temp);
				}
				else {
					StringBuffer temp = new StringBuffer("s188708 Michal Mroz\n");
					credits.add(temp);
				}
				
			}
			
			
			ArrayList<Integer> rozm = new ArrayList<Integer>();
			rozm.add(x); rozm.add(y);
			
			FileIO fileio = new FileIO();
			
			ArrayList<StringBuffer> plansz = new ArrayList<StringBuffer>();
			for(int i=0; i<y; i++) {
				
				StringBuffer temp = new StringBuffer();
				
				for(int j=0; j<x; j++) {
					temp.append(' ');
				}
				
				plansz.add(temp);
			}
			
			Swiat swiat = new Swiat(rozm, plansz, credits);
			
			swiat.setIsHex(isHex);
			
			ArrayList<ArrayList<Organizm>> organizmy = new ArrayList<ArrayList<Organizm>>();
			
			for(int i=0; i < y; i++) {
				ArrayList<Organizm> temp = new ArrayList<Organizm>(x);
				organizmy.add(temp);
			}
			
			if(!swiat.getIsHex()) {
			
				int cPosY = y/2;
				int cPosX = x/2;
				
				for(int i=0; i < y; i++) {
					for(int j=0; j < x; j++) {
						if(i == cPosY && j == cPosX) {
							ArrayList<Integer> temp = new ArrayList<Integer>();
							temp.add(j); temp.add(i);
							Organizm czlowiek = new Czlowiek(swiat, temp);
							organizmy.get(i).add(czlowiek);
							continue;
						}
						swiat.partitionOrganizm(i, j, organizmy);
					}
				}
			
			}
			
			
			
			Boolean flag = true;
				
			gu.setUpButtonListeners();
			
			
			while(flag) {
				
				gu.updateData(swiat, organizmy);
				
				gu.setUpGUI();
				
				gu.setUpKeyListeners();
							
				for (int i = 0; i < 50; ++i) System.out.println();
				
				swiat.rysujSwiat();
				
				Boolean czyCzlowiekIstnieje = false;
				if(swiat.findOrganizmByChar('C', organizmy) != organizmy.get(0).get(0)) {
					swiat.findOrganizmByChar('C', organizmy).podajKierunekRuchu();
					swiat.findOrganizmByChar('C', organizmy).podajInfoTarcza(swiat.getTuraUmiejetnosc());
					czyCzlowiekIstnieje = true;
				}
				
				else {
					System.out.println("Czlowiek nie zyje!");
					czyCzlowiekIstnieje = false;
				}
				
				
				do {
					Thread.sleep(10);
				} while(swiat.getButtonWait());
				
				
				swiat.changeButtonWait(true);
				
				
				if(swiat.getIsSave()) {
					
					MyResult temp = fileio.readSave(swiat, organizmy);
					
					swiat.changeIsSave(false);
					
					if(temp != null) {
								
						TimeUnit.SECONDS.sleep(1);
								
						x = temp.getFirst().get(0);
								
						y = temp.getFirst().get(1);
								
						organizmy = temp.getSecond();
								
						swiat.changeTuraUmiejetnosc(temp.getFirst().get(2));
								
						if(swiat.findOrganizmByChar('C', organizmy) != organizmy.get(0).get(0)) {
							Organizm temp2 = swiat.findOrganizmByChar('C', organizmy);
							temp2.zmienKierunekRuchu(temp.getFirst().get(3));
							temp2.zmienStanTarczyAldura(temp.getFirst().get(4) == 1 ? true : false);
						}
								
						czyCzlowiekIstnieje = temp.getFirst().get(5) == 1 ? true : false;
					}
					
				}
						
			}
			
		}

	}
	

