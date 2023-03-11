import java.util.*;

public class Main {

    private static final double pi = 3.14159f;

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();

        int prod = a * b;

        System.out.println("PROD = " + prod);
    }
}