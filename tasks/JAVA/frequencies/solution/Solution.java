public class Solution {

    public int[] frequencies(int[] numbers) {
        int[] result = new int[100];
        for (int number : numbers) {
            result[number]++;
        }
        return result;
    }
}
