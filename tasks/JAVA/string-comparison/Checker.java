import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.List;
import java.util.Collections;
import java.util.ArrayList;

public class Checker {

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String sortType = reader.readLine();
        int n = Integer.parseInt(reader.readLine());
        List<String> strings = new ArrayList<String>();
        for (int i = 0; i < n; i++) {
            strings.add(reader.readLine());
        }
        Comparator<String> comparator = new Solution().getComparator(sortType);
        Collections.sort(strings, comparator);
        for (String string : strings) {
            System.out.println(string);
        }
    }
}
