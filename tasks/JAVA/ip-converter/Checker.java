import java.io.*;

public class Checker {

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String address = reader.readLine();
        Solution sol = new Solution();
        System.out.println(sol.ipToDec(address));
        System.out.println(sol.ipToHex(address).toLowerCase());
        System.out.println(sol.ipToBin(address));
    }
}
