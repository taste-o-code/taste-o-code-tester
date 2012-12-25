import java.util.*;
import java.io.*;

public class Checker {

    private static Map<String, List<String>> readData() throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        Map<String, List<String>> data = new HashMap<String, List<String>>(n);
        for (int i = 0; i < n; i++) {
            String name = reader.readLine();
            int m = Integer.parseInt(reader.readLine());
            List<String> desserts = new ArrayList<String>(m);
            for (int j = 0; j < m; j++) {
                desserts.add(reader.readLine().trim());
            }
            data.put(name, desserts);
        }
        return data;
    }

    private static void printResults(Map<String, Integer> frequencies) {
        Map<String, Integer> sorted = new TreeMap<String, Integer>(frequencies);
        for (Map.Entry<String, Integer> entry : sorted.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }

    public static void main(String[] args) throws Exception {
        Map<String, List<String>> data = readData();
        Map<String, Integer> frequencies = new Solution().dessertFrequencies(data);
        printResults(frequencies);
    }
}
