import java.util.*;

public class Main {

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        double a = scan.nextFloat() * 2;
        double b = scan.nextFloat() * 3;
        double c = scan.nextFloat() * 5;

        double med = (a+b+c) / 10;

        System.out.println(String.format("MEDIA = %.1f", med));
    }
}
