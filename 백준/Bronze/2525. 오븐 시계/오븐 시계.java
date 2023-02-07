import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int M = sc.nextInt();
		int plus = sc.nextInt();
		sc.close();
		M+=plus;
		while(M>=60) {
			h++;
			M-=60;
		}
		while(h>=24)h-=24;
		System.out.print(h+" "+M);
		
	}
}