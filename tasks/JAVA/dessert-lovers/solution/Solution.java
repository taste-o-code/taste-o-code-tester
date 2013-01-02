import java.util.*;

public class DessertLovers {


    public Map<String, Integer> dessertFrequencies(Map<String, List<String>> desserts) {
        Map<String, Integer> result = new HashMap<String, Integer>();
        for (List<String> list : desserts.values()) {
            for (String dessert : list) {
                if (result.containsKey(dessert)) {
                    result.put(dessert, result.get(dessert) + 1);
                } else {
                    result.put(dessert, 1);
                }
            }
        }
        return result;
    }
}
