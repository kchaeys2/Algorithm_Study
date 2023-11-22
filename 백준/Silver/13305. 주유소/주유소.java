import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt();
		long[] km = new long[N-1];
		long[] one = new long[N];
		for(int i=0;i<N-1;i++) {
			km[i]=sc.nextLong();
		}
		for(int i=0;i<N;i++) {
			one[i] = sc.nextLong();
		}
		sc.close();
		
		long min = one[0];
		long sum =0;
		
		for(int i=0;i<N-1;i++) {
			if(one[i]<=min) min = one[i];
			sum+=km[i]*min;
		}
		
		System.out.print(sum);
		
	}
}