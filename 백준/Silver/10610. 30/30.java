import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String n = sc.next();

		int len = n.length();
		int[] arr = new int[len];
		
		int sum = 0;
		for(int i=0;i<len;i++) {
			arr[i]=n.charAt(i)-'0';
			sum += arr[i];
		}
		Arrays.sort(arr);
		if(arr[0]==0&&sum%3==0) {
			for(int i=len-1;i>=0;i--) {
				System.out.print(arr[i]);
			}
		}
		else System.out.print(-1);

	}
}