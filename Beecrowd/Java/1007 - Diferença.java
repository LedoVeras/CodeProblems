import java.util.*;

public class Main {

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        int d = scan.nextInt();

        int toReturn = (a * b - c * d);

        System.out.println("DIFERENCA = " + toReturn);
    }
}