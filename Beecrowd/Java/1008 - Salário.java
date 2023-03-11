import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int numb = scan.nextInt();
        int hour = scan.nextInt();
        float perHour = scan.nextFloat();

        float salary = hour * perHour;

        System.out.println("NUMBER = " + numb);
        System.out.println(String.format("SALARY = U$ %.2f", salary));
    }
}