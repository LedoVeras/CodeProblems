import java.util.*;

public class Main {

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        double a = scan.nextFloat();
        double b = scan.nextFloat();

        double med = (a * 3.5f + b * 7.5f) / 11;

        System.out.println(String.format("MEDIA = %.5f", med));
    }
}