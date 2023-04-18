import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int one = scanner.nextInt();
        int two = scanner.nextInt();

        if(one > two) {
            System.out.println(">");
        } else if(one == two) {
            System.out.println("==");
        } else {
            System.out.println("<");
        }

    }
}
