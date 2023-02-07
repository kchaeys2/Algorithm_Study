import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		 int n = sc.nextInt();
		 int k = sc.nextInt();
		 int[] coin = new int[n];
		 int count = 0;
		 
		 for(int i =0;i<n;i++) {
			 coin[i]=sc.nextInt();
		 }

		 for(int i=n-1;i>=0;i--) {
              if(k==0) break;
			  else if(coin[i]<=k) {
				 count+=k/coin[i];
				 k%=coin[i];
			 }
		 }
		 System.out.print(count);
	}
}
