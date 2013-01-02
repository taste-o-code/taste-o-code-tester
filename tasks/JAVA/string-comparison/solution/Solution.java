import java.util.Comparator;

public class StringComparison {

    public static enum StringComparator implements Comparator<String> {
        ASCENDING {
            public int compare(String a, String b) {
                return a.compareTo(b);
            }
        },
        DESCENDING {
            public int compare(String a, String b) {
                return b.compareTo(a);
            }
        },
        BYLENGTH {
            public int compare(String a, String b) {
                return a.length() - b.length();
            }
        },
        BYWORDCOUNT {
            public int compare(String a, String b) {
                return a.split(" ").length - b.split(" ").length;
            }
        }
    }

    public Comparator<String> getComparator(String type) {
        return StringComparator.valueOf(StringComparator.class, type.toUpperCase());
    }
}
