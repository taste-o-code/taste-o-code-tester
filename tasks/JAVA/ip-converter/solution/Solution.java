public class Solution {

    private int[] parse(String address) {
        String[] parts = address.split("\\.");
        int[] result = new int[4];
        int radix = parts[0].length() == 8 ? 2 : parts[0].toLowerCase().startsWith("0x") ? 16 : 10;
        for (int i = 0; i < 4; i++) {
            result[i] = Integer.parseInt(radix != 16 ? parts[i] : parts[i].substring(2), radix);
        }
        return result;
    }

    private String join(String[] parts) {
        StringBuilder stb = new StringBuilder();
        for (int i = 0; i < parts.length; i++) {
            stb.append(parts[i]);
            if (i != parts.length - 1) {
                stb.append(".");
            }
        }
        return stb.toString();
    }

    public String ipToDec(String address) {
        int[] parts = parse(address);
        String[] res = new String[4];
        for (int i = 0; i < 4; i++) {
            res[i] = String.valueOf(parts[i]);
        }
        return join(res);
    }

    public String ipToHex(String address) {
        int[] parts = parse(address);
        String[] res = new String[4];
        for (int i = 0; i < 4; i++) {
            res[i] = String.format("%#04x", parts[i]);
        }
        return join(res);
    }

    public String ipToBin(String address) {
        int[] parts = parse(address);
        String[] res = new String[4];
        for (int i = 0; i < 4; i++) {
            String val = Integer.toBinaryString(parts[i]);
            while (val.length() < 8) {
                val = "0" + val;
            }
            res[i] = val;
        }
        return join(res);
    }

    public static void main(String[] args) {
        String ip = "10001011.10001100.00010001.01001111";
        Solution sol = new Solution();
        System.out.println(sol.ipToDec(ip));
        System.out.println(sol.ipToHex(ip));
        System.out.println(sol.ipToBin(ip));
    }
}
