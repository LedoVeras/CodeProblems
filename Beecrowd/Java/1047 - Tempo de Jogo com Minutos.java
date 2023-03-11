import java.util.*;

public class Main {

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int hrI = scan.nextInt();
        int miI = scan.nextInt();
        int hrF = scan.nextInt();
        int miF = scan.nextInt();

        int hourDif = hrF - hrI;
        int minDif = miF - miI;

        int hrTotal = hourDif < 0 || (hourDif == 0 && minDif <= 0)? 24 + hourDif : hourDif;

        int minTotal = minDif;

        if(minDif < 0){
            hrTotal--;
            minTotal = 60 + minDif;
        }

        System.out.println("O JOGO DUROU " + hrTotal + " HORA(S) E " + minTotal + " MINUTO(S)");
    }
}