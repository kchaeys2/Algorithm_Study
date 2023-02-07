import java.util.Scanner;
import java.util.LinkedList;

class Graph{
	class Node {
		int data;
		LinkedList<Node> adjacent;
		boolean marked;
		Node(int data){ //Node생성자
			this.data = data;
			this.marked = false;
			adjacent = new LinkedList<Node>();
		}
	}
	Node[] nodes;//Node저장소
	Graph(int size){//Graph생성자
		nodes = new Node[size+1];
		for(int i=1;i<size+1;i++) {//nodes[0]은 데이터가 없다.
			nodes[i] = new Node(i);
		}
	}
	
	void addEdge(int a,int b) {//연결
		Node n1 = nodes[a];
		Node n2 = nodes[b];
		if(!n1.adjacent.contains(n2)) n1.adjacent.add(n2);
		if(!n2.adjacent.contains(n1)) n2.adjacent.add(n1);
	}
	public int sum=-1;
	void dfs(Node r) {
		if(r==null)return;
		r.marked = true;
		sum+=1;
		for(Node n:r.adjacent) {
			if(n.marked ==false) dfs(n);
		}
	}
	void dfs(int index) {
		Node r = nodes[index];
		dfs(r);
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int addNum = sc.nextInt();
		
		Graph graph = new Graph(num);
		int a;
		int b;
		for(int i=0;i<addNum;i++) {
			a = sc.nextInt();
			b = sc.nextInt();
			graph.addEdge(a, b);
		}
		sc.close();
		graph.dfs(1);
		System.out.print(graph.sum);
		
	}
}