import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class FileIO{
	
	public void makeSave(int x, int y, ArrayList<ArrayList<Organizm>> organizmy, int turaUmiejetnosc, Boolean czyCzlowiekIstnieje, Boolean czyJestTarczaAldura, int kierunekRuchu, int obecnaTura) {
		
		try {
			BufferedWriter writer = new BufferedWriter(new FileWriter("save.txt"));
			
			int czyCzlowiekIstniejeInt = czyCzlowiekIstnieje ? 1 : 0;
			int czyJestTarczaAlduraInt = czyJestTarczaAldura ? 1 : 0;
			
			writer.write("x " + Integer.toString(x));
			writer.write("\ny " + Integer.toString(y));
			writer.write("\nt " + Integer.toString(obecnaTura));
			writer.write("\nc " + Integer.toString(turaUmiejetnosc) + " " + Integer.toString(kierunekRuchu) + " " + Integer.toString(czyJestTarczaAlduraInt) + " " + Integer.toString(czyCzlowiekIstniejeInt));
			
			for(int Y=0; Y < organizmy.size(); Y++) {
				for(int X=0; X < organizmy.get(Y).size(); X++) {
					Organizm temp = organizmy.get(Y).get(X);
					
					writer.write("\no " +  temp.getZnak() + " " + temp.getPolozenie(0) + " " + temp.getPolozenie(1) + " " + temp.getSila() + " " + temp.getInicjatywa() + " " + temp.getWiek());
				}
			}
			
			writer.close();
		} 
		
		
		catch(IOException e) {
			e.printStackTrace();
		}
		
	}
	
	public MyResult readSave(Swiat swiat, ArrayList<ArrayList<Organizm>> organizmy) throws InterruptedException {
		File f = new File("save.txt");
			
		if(f.exists() && !f.isDirectory()) {
			
			try {
				BufferedReader reader = new BufferedReader(new FileReader("save.txt"));
				
				String line;
				
				ArrayList<Integer> ret = new ArrayList<Integer>();
				
				int x = 0;
				int y = 0;
				
				Boolean gotX = false;
				Boolean gotY = false;
				Boolean alreadySet = false;
				
				ArrayList<StringBuffer> planszNew = new ArrayList<StringBuffer>();
				
				ArrayList<StringBuffer> creditsNew = new ArrayList<StringBuffer>();
				
				ArrayList<ArrayList<Organizm>> organizmyNew = new ArrayList<ArrayList<Organizm>>();
					
				while((line = reader.readLine()) != null) {
					
					if(gotX && gotY && (alreadySet == false)) {
						
						for(int i=0; i < y; i++) {
							ArrayList<Organizm> temp = new ArrayList<Organizm>();
							organizmyNew.add(temp);
						}
						
						for(int i=0; i<3; i++) {
							if(!(i % 2 > 0)) {
								char[] chars = new char[x + 1];
								Arrays.fill(chars, '-');
								chars[x] = '\n';
								String s = new String(chars);
								StringBuffer temp = new StringBuffer(s);
								creditsNew.add(temp);
							}
							
							else {
								StringBuffer temp = new StringBuffer("s188708 Michal Mroz\n");
								creditsNew.add(temp);
							}
							
						}
						
						
						for(int i=0; i<y; i++) {
							
							StringBuffer temp = new StringBuffer();
							
							for(int j=0; j<x; j++) {
								temp.append(' ');
							}
							
							planszNew.add(temp);
						}
						
						for(int i=0; i<swiat.getRozmiarY(); i++) {
							swiat.getPlansza().add(new StringBuffer());
							for(int j=0; j<swiat.getRozmiarX(); j++) {
								swiat.getPlansza().get(i).append(" ");
							}
						}
											
						alreadySet = true;
					}
					

					switch(line.charAt(0)) {
						case 'x':
							x = Integer.parseInt(line.substring(2));
							ret.add(x);
							swiat.changeRozmiarX(x);
							gotX = true;
							break;
						case 'y':
							y = Integer.parseInt(line.substring(2));
							ret.add(y);
							swiat.changeRozmiarY(y);
							gotY = true;
							break;
						case 't':
							int t = Integer.parseInt(line.substring(2));
							swiat.changeObecnaTura(t);
							break;
						case 'c':
							int fromIndex = 0;
							
							while(line.indexOf(' ', line.indexOf(' ', fromIndex) + 1) != -1) {
								int v = Integer.parseInt(line.substring(line.indexOf(' ', fromIndex) + 1, line.indexOf(' ', line.indexOf(' ', fromIndex) + 1)));
								
								ret.add(v);
								
								fromIndex = line.indexOf(' ', fromIndex) + 1; 
							}
							
							ret.add(Integer.parseInt(line.substring(line.indexOf(' ', fromIndex) + 1)));
							
							break;
							
							
						case 'o':
	
							Organizm temp = null;
							
							int FI = 2;
							
							ArrayList<Integer> values = new ArrayList<Integer>();
							
							while(line.indexOf(' ', line.indexOf(' ', FI) + 1) != -1) {
								int v = Integer.parseInt(line.substring(line.indexOf(' ', FI) + 1, line.indexOf(' ', line.indexOf(' ', FI) + 1)));
								values.add(v);
								FI = line.indexOf(' ', FI) + 1; 
							}
							
							values.add(Integer.parseInt(line.substring(line.indexOf(' ', FI) + 1)));
							
							ArrayList<Integer> tempL = new ArrayList<Integer>();
							tempL.add(values.get(0)); tempL.add(values.get(1));
							
							switch(line.charAt(2)) {
								case 'A':
									temp = new Antylopa(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'B':
									temp = new Barszcz(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'C':
									temp = new Czlowiek(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'G':
									temp = new Guarana(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'J':
									temp = new Jagody(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'L':
									temp = new Lis(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'M':
									temp = new Mlecz(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'O':
									temp = new Owca(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'T':
									temp = new Trawa(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'W':
									temp = new Wilk(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
								case 'Z':
									temp = new Zolw(swiat, tempL, values.get(4), values.get(3), values.get(2));
									break;
							}
							
							planszNew.get(values.get(1)).replace(values.get(0), values.get(0) + 1, ""+line.charAt(2));
							
							organizmyNew.get(values.get(1)).add(temp);
							
							//organizmyNew.get(values.get(1)).get(organizmy.get(values.get(1)).size() - 1).changePolozenie(values.get(0), values.get(1));
							
							break;
					}
					
				}
							
				swiat.changePlansza(planszNew);
				
				swiat.changeCredits(creditsNew);
				
				TimeUnit.SECONDS.sleep(1);
					
				reader.close();
				
				return new MyResult(ret, organizmyNew);
			} 
			
			
			
			catch (IOException e) {
				e.printStackTrace();
				return null;
			}
			
		}
		
		else {
			System.out.println("Zapis nie istnieje!");
			TimeUnit.SECONDS.sleep(1);
			return null;
		}
		
		
	}

}
