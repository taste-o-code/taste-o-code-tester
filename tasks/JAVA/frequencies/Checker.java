import java.util.Scanner;
import java.util.Arrays;

public class Checker {

    public static int[] correctSolution(int[] numbers) {
        int[] result = new int[100];
        for (int number : numbers) {
            result[number]++;
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt();
        }
        int[] correct = correctSolution(numbers);
        int[] usersAnswer = new Frequencies().frequencies(numbers);
        boolean result = Arrays.equals(correct, usersAnswer);
        System.out.println(result);
    }
}
