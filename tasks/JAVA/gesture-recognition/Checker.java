import java.awt.Point;
import java.util.*;
import java.io.*;

public class Checker {

    private static Point[][] readInput() throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = sc.nextInt();
        Point[][] points = new Point[t][n];
        for (int i = 0; i < t; i++) {
            for (int j = 0; j < n; j++) {
                points[i][j] = new Point(sc.nextInt(), sc.nextInt());
            }
        }
        sc.close();
        return points;
    }

    public static void main(String[] args) throws Exception {
        Point[][] data = readInput();
        GestureRecognition.Gesture result = new GestureRecognition().recognize(data);
        System.out.println(result.name());
    }
}
