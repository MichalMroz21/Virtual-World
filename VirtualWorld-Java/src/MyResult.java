import java.util.ArrayList;

final class MyResult {
    private final ArrayList<Integer> first;
    private final ArrayList<ArrayList<Organizm>> second;

    public MyResult(ArrayList<Integer> first, ArrayList<ArrayList<Organizm>> second) {
        this.first = first;
        this.second = second;
    }

    public ArrayList<Integer> getFirst() {
        return first;
    }

    public ArrayList<ArrayList<Organizm>> getSecond() {
        return second;
    }
}
