import java.util.Arrays;
import java.util.Scanner;
public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] people = new int[num];
		for(int i=0;i<num;i++) {
			people[i] = sc.nextInt();
		}
		Arrays.sort(people);
		int sum = 0;
		int aSum = 0;
		for(int i=0;i<num;i++) {
			sum+=people[i];
			aSum+=sum;
		}
		System.out.print(aSum);
	}
}
