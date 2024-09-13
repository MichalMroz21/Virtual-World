import java.util.Comparator;

public class MyComparator implements Comparator<Organizm>{
	
	@Override
	public int compare(Organizm a, Organizm b) {
		return (int) (a.getWiek() - b.getWiek());
	}
}
