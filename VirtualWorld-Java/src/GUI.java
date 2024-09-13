import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.FlowLayout;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.WindowEvent;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSpinner;
import javax.swing.JSplitPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SpinnerModel;
import javax.swing.SpinnerNumberModel;
import javax.swing.Timer;

import java.awt.Color;
import java.awt.Component;

public class GUI{
	
	private JFrame frame;
	private JButton nastepnaTura;
	private JButton wyjscie;
	private JButton zapisz;
	private JButton zaladuj;
	private JButton umiejetnosc;
	private JPanel panel1;
	private JPanel panel2;
	private JSplitPane splitpane;
	private JLabel text1;
	private JLabel text2;
	private JLabel text3;
	private JCheckBox chbox;
	private SpinnerModel model;
	private JSpinner spinnerX;
	private JSpinner spinnerY;
	private JFrame frameStart;
	private JButton acceptButton;
	private JPanel panelStart;
	private JLabel textX;
	private JLabel textY;
	private JLabel hex;
	private SpinnerModel model2;
	
	private Boolean isChecked;
	private Boolean isStart;
	
	private int width;
	private int height;
	
	private Swiat swiat;
	private ArrayList<ArrayList<Organizm>> organizmy;
	
	public Boolean getIsStart() {
		return isStart;
	}
	
	public int getWidth() {
		return width;
	}
	
	public int getHeight() {
		return height;
	}
	
	public Boolean getIsChecked() {
		return isChecked;
	}
	
	public GUI() {
		
		isStart = true;
		
		frame = new JFrame();
		panel1 = new JPanel();
		panel2 = new JPanel();
		text1 = new JLabel();
		text2 = new JLabel();
		text3 = new JLabel();
		
		textX = new JLabel("Wspolrzedne X");
		textY = new JLabel("Wspolrzedne Y");
		hex = new JLabel("Czy ma byc plansza w ksztalcie HEX?");
		
		chbox = new JCheckBox();
		model = new SpinnerNumberModel(1, 1, 100, 1);     
		model2 = new SpinnerNumberModel(1, 1, 100, 1);
		spinnerX = new JSpinner(model);
	    spinnerY = new JSpinner(model2);
		frameStart = new JFrame();
		panelStart = new JPanel();
		acceptButton = new JButton("Zacznij gre");
		
		nastepnaTura = new JButton("Nastepna tura");
		wyjscie = new JButton("Wyjscie");
		zapisz = new JButton("Zapisz stan gry");
		zaladuj = new JButton("Zaladuj stan gry");
		umiejetnosc = new JButton("Uzyj umiejetnosci");
		splitpane = new JSplitPane(JSplitPane.VERTICAL_SPLIT, panel1, panel2);

	}
	
	public void setUpStartingGUI() {
		
		Container cp = frame.getContentPane();

		panelStart.setLayout(new BoxLayout(panelStart, BoxLayout.Y_AXIS));
		
		textX.setAlignmentX(Component.CENTER_ALIGNMENT);
		spinnerX.setAlignmentX(Component.CENTER_ALIGNMENT);
		textY.setAlignmentX(Component.CENTER_ALIGNMENT);
		spinnerY.setAlignmentX(Component.CENTER_ALIGNMENT);
		hex.setAlignmentX(Component.CENTER_ALIGNMENT);
		chbox.setAlignmentX(Component.CENTER_ALIGNMENT);
		acceptButton.setAlignmentX(Component.CENTER_ALIGNMENT);
		
		acceptButton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				
				try {
					spinnerX.commitEdit();
				} catch (ParseException e1) {
					e1.printStackTrace();
				}
				try {
					spinnerY.commitEdit();
				} catch (ParseException e1) {
					e1.printStackTrace();
				}
				
				String value = spinnerX.getValue() + "";
				width =Integer.parseInt(value);
				System.out.println(width);
				value = spinnerY.getValue() + "";
				height = Integer.parseInt(value);
				
				isChecked = chbox.isSelected();

				frameStart.setVisible(false);
				
				isStart = false;
				
				
			}
		
		});
		
		
		panelStart.add(textX);
		panelStart.add(spinnerX);
		panelStart.add(textY);
		panelStart.add(spinnerY);
		panelStart.add(hex);
		panelStart.add(chbox);
		panelStart.add(acceptButton);
		
		frameStart.add(panelStart);
		
		frameStart.setSize(1920, 1080);
		frameStart.setTitle("GUI");
		frameStart.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		frameStart.setExtendedState(frameStart.getExtendedState() | JFrame.MAXIMIZED_BOTH);
		
		frameStart.setVisible(true);
	}

	public void setUpGUI() throws InterruptedException {
				
		panel1.removeAll ();
		
		Container cp = frame.getContentPane();
		
		cp.add(splitpane);
		
		GridLayout grid = new GridLayout(swiat.getRozmiarY(), swiat.getRozmiarX());
		
		panel1.setLayout(grid);
		panel2.setLayout(new BoxLayout(panel2, BoxLayout.Y_AXIS));
		
		ArrayList<StringBuffer> plansza = swiat.getPlansza();
		
		
		for(int i=0; i<swiat.getRozmiarY(); i++) {
			
			for(int j=0; j<swiat.getRozmiarX(); j++) {
				
				JLabel tile = new JLabel();
				tile.setOpaque(true);
				
				Color color = Color.white;
				
				switch(plansza.get(i).charAt(j)) {
					case ' ':
						color = Color.white;
						break;
					case 'A':
						color = Color.orange;
						break;
					case 'B':
						color = Color.red;
						break;
					case 'C':
						color = Color.pink;
						break;
					case 'G':
						color = Color.gray;
						break;
					case 'J':
						color = Color.magenta;
						break;
					case 'L':
						color = Color.blue;
						break;
					case 'M':
						color = Color.lightGray;
						break;
					case 'O':
						color = Color.darkGray;
						break;
					case 'T':
						color = Color.green;
						break;
					case 'W':
						color = Color.black;
						break;
					case 'Z':
						color = Color.cyan;
						break;
				}
				
				int a = i;
				int b = j;
				
				tile.setBackground(color);			
				
				tile.addMouseListener(new MouseListener() {
					
					public Color c = tile.getBackground();
					final int y = a;
					final int x = b;
					
					int n = 0;
					char ch = ' ';
					
					public Color selection = color.white;
					JLabel t = null;
					
					Timer timer;

					@Override
					public void mouseClicked(MouseEvent e) {
						swiat.addOrganizmByXY(x, y, organizmy, ch);
						swiat.changeButtonWait(false);	
					}

					@Override
					public void mousePressed(MouseEvent e) {
					}

					@Override
					public void mouseReleased(MouseEvent e) {						
					}
					
					ActionListener changeColors = new ActionListener() {
						public void actionPerformed(ActionEvent evt) {
							
							if(n == 10) {
								n = 1;
							}
							else {
								n++;
							}
														
							switch(n) {
								case 1:
									ch = 'A';
									selection = Color.orange;
									break;
								case 2:
									ch = 'B';
									selection = Color.red;
									break;
								case 3:
									ch = 'G';
									selection = Color.gray;
									break;
								case 4:
									ch = 'J';
									selection = Color.magenta;
									break;
								case 5:
									ch = 'L';
									selection = Color.blue;
									break;
								case 6:
									ch = 'M';
									selection = Color.lightGray;
									break;
								case 7:
									ch = 'O';
									selection = Color.darkGray;
									break;
								case 8:
									ch = 'T';
									selection = Color.green;
									break;
								case 9:
									ch = 'W';
									selection = Color.black;
									break;
								case 10:
									ch = 'Z';
									selection = Color.cyan;
									break;
							}
							t.setBackground(selection);
						}
					};

					@Override
					public void mouseEntered(MouseEvent e) {
						
						timer = new Timer(700, changeColors);
						timer.setRepeats(true);
						timer.start();
						t = (JLabel) e.getSource();					
					}

					@Override
					public void mouseExited(MouseEvent e) {
						timer.stop();
						selection = color.white;
						n = 0;
						ch = ' ';
						
						JLabel tile = (JLabel) e.getSource();
						tile.setBackground(c);
						
					}
									
				});
				
							
				panel1.add(tile);
			}	
		}		
		
		
		panel2.add(nastepnaTura);
		panel2.add(wyjscie);
		panel2.add(zapisz);
		panel2.add(zaladuj);
		panel2.add(umiejetnosc);
		
		if(swiat.findOrganizmByChar('C', organizmy) != organizmy.get(0).get(0)) {
			text1.setText(swiat.findOrganizmByChar('C', organizmy).podajKierunekRuchu());
			text2.setText(swiat.findOrganizmByChar('C', organizmy).podajInfoTarcza(swiat.getTuraUmiejetnosc()));
		}
		else {
			text1.setText("Czlowiek nie zyje!");
			text2.setText("");
		}
		
		text3.setText("Obecna tura: " + swiat.getObecnaTura());
		
		panel2.add(text1);
		panel2.add(text2);
		panel2.add(text3);
				
		nastepnaTura.setAlignmentX(Component.CENTER_ALIGNMENT);
		wyjscie.setAlignmentX(Component.CENTER_ALIGNMENT);
		zapisz.setAlignmentX(Component.CENTER_ALIGNMENT);
		zaladuj.setAlignmentX(Component.CENTER_ALIGNMENT);
		umiejetnosc.setAlignmentX(Component.CENTER_ALIGNMENT);
		
		text1.setAlignmentX(Component.CENTER_ALIGNMENT);
		text2.setAlignmentX(Component.CENTER_ALIGNMENT);
		text3.setAlignmentX(Component.CENTER_ALIGNMENT);
				
		frame.setSize(1920, 1080);
		frame.setTitle("GUI");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		frame.addKeyListener(new KeyListener() {
			
			@Override
			public void keyTyped(KeyEvent e) {
				
			}
			
			@Override
			public void keyPressed(KeyEvent e) {
				int keyCode = e.getKeyCode();
				
				Boolean czyCzlowiekIstnieje = true;
				if(swiat.findOrganizmByChar('C', organizmy) == organizmy.get(0).get(0)) czyCzlowiekIstnieje = false;
				
				switch(keyCode) {
					case KeyEvent.VK_UP:
						if (czyCzlowiekIstnieje) {
							swiat.findOrganizmByChar('C', organizmy).zmienKierunekRuchu(1);
						}
						break;
					case KeyEvent.VK_DOWN:
						if (czyCzlowiekIstnieje) {
							swiat.findOrganizmByChar('C', organizmy).zmienKierunekRuchu(2);
						}
						break;
					case KeyEvent.VK_LEFT:
						if (czyCzlowiekIstnieje) {
							swiat.findOrganizmByChar('C', organizmy).zmienKierunekRuchu(3);
						}
						break;
					case KeyEvent.VK_RIGHT:
						if (czyCzlowiekIstnieje) {
							swiat.findOrganizmByChar('C', organizmy).zmienKierunekRuchu(4);
						}
						break;
				}
				swiat.changeButtonWait(false);
			}
			
			@Override
			public void keyReleased(KeyEvent e) {
				
			}
			
		});
		
		frame.setExtendedState(frame.getExtendedState() | JFrame.MAXIMIZED_BOTH);
			
		frame.setVisible(true);
		
		splitpane.setDividerLocation(.75);
			
	}
	
	public void setUpButtonListeners() {
		
		ActionListener buttonListener = new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent ae){
				
				if(ae.getSource() == nastepnaTura) {
					
					Boolean czyCzlowiekIstnieje = true;
					if(swiat.findOrganizmByChar('C', organizmy) == organizmy.get(0).get(0)) czyCzlowiekIstnieje = false;
					
					if (czyCzlowiekIstnieje) {

						if (swiat.findOrganizmByChar('C', organizmy).getKierunekRuchu() == 0) {
							System.out.println("Podaj strzalkami kierunek ruchu czlowieka przed rozpoczeciem tury!");
							try {
								TimeUnit.SECONDS.sleep(1);
							} catch (InterruptedException e) {
								e.printStackTrace();
							}
							
						}

						else {
							try {
								swiat.wykonajTure(swiat, swiat.getRozmiarX(), swiat.getRozmiarY(), organizmy);
							} catch (InterruptedException e) {
								e.printStackTrace();
							}

							if (swiat.getTuraUmiejetnosc() != -5) swiat.changeTuraUmiejetnosc(swiat.getTuraUmiejetnosc() - 1);

							if (czyCzlowiekIstnieje && swiat.getTuraUmiejetnosc() == 0) {
								swiat.findOrganizmByChar('C', organizmy).zmienStanTarczyAldura(false);
							}
							
						}
					}

					else {

						try {
							swiat.wykonajTure(swiat, swiat.getRozmiarX(), swiat.getRozmiarY(), organizmy);
						} catch (InterruptedException e) {
							e.printStackTrace();
						}

						if (swiat.getTuraUmiejetnosc() != -5) swiat.changeTuraUmiejetnosc(swiat.getTuraUmiejetnosc() - 1);

						if (czyCzlowiekIstnieje && swiat.getTuraUmiejetnosc() == 0 && swiat.findOrganizmByChar('C', organizmy) != organizmy.get(0).get(0)) {
							swiat.findOrganizmByChar('C', organizmy).zmienStanTarczyAldura(false);
						}
						

					}
					
					swiat.changeButtonWait(false);
				}
				
				
				else if(ae.getSource() == wyjscie){
					frame.dispatchEvent(new WindowEvent(frame, WindowEvent.WINDOW_CLOSING));
				}
				else if(ae.getSource() == zapisz){
					
					Boolean czyCzlowiekIstnieje = true;
					if(swiat.findOrganizmByChar('C', organizmy) == organizmy.get(0).get(0)) czyCzlowiekIstnieje = false;
					
					FileIO fileio = new FileIO();
					
					if(swiat.findOrganizmByChar('C', organizmy) != organizmy.get(0).get(0)) {
						Organizm temp = swiat.findOrganizmByChar('C', organizmy);
						fileio.makeSave(swiat.getRozmiarX(), swiat.getRozmiarY(), organizmy, swiat.getTuraUmiejetnosc(), czyCzlowiekIstnieje, temp.czyJestTarczaAldura(), temp.getKierunekRuchu(), swiat.getObecnaTura());
					}
					else {
						fileio.makeSave(swiat.getRozmiarX(), swiat.getRozmiarY(), organizmy, swiat.getTuraUmiejetnosc(), czyCzlowiekIstnieje, false, 0, swiat.getObecnaTura());
					}
					
					swiat.changeButtonWait(false);
					
				}
				else if(ae.getSource() == zaladuj){
					
					swiat.changeButtonWait(false);
					swiat.changeIsSave(true);
					
				}
				else if(ae.getSource() == umiejetnosc){
					
					if(swiat.findOrganizmByChar('C', organizmy) != organizmy.get(0).get(0)) {
						if (swiat.getTuraUmiejetnosc() == -5) {
							swiat.findOrganizmByChar('C', organizmy).zmienStanTarczyAldura(true);
							swiat.changeTuraUmiejetnosc(5);
						}
					}
					
					swiat.changeButtonWait(false);
					
				}
				
			}
			
		};
		
		nastepnaTura.addActionListener(buttonListener);
		wyjscie.addActionListener(buttonListener);
		zapisz.addActionListener(buttonListener);
		zaladuj.addActionListener(buttonListener);
		umiejetnosc.addActionListener(buttonListener);
		
	}
	
	public void setUpKeyListeners() {
		
		frame.requestFocusInWindow();
		
	}
	
	public void updateData(Swiat sw, ArrayList<ArrayList<Organizm>> org) {
		swiat = sw;
		organizmy = org;
	}
	
	
}
