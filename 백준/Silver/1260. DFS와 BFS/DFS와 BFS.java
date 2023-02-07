import java.util.Queue;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;

class Graph{
	class Node {
		int data;
		ArrayList<Node> adjacent;
		boolean marked;
		Node(int data){ //Node생성자
			this.data = data;
			this.marked = false;
			adjacent = new ArrayList<Node>();
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
	class sort implements Comparator<Node>{//Collection.sort쓸려고 한거
		public int compare(Node n1,Node n2) {
			if(n1.data>n2.data) return 1;
			else if(n1.data<n2.data) return -1;
			return 0;
		}
	}

	void dfs(Node r) {
		if(r==null)return;
		r.marked = true;
		System.out.print(r.data+" ");
		Collections.sort(r.adjacent,new sort());
		for(Node n:r.adjacent) {
			if(n.marked ==false) dfs(n);
		}
	}
	void dfs(int index) {
		Node r = nodes[index];
		dfs(r);
	}

	void bfs(int index) {
		for(int i=1;i<nodes.length;i++) {
			nodes[i].marked = false;
		}
		Node root = nodes[index];
		Queue<Node> queue = new LinkedList<>();
		queue.add(root);
		root.marked=true;

		while(!queue.isEmpty()) {
			Node r = queue.remove();

			Collections.sort(r.adjacent,new sort());
			for(Node n:r.adjacent) {
				if(n.marked == false) {
					n.marked = true;
					queue.add(n);
				}
			}
			System.out.print(r.data+" ");
		}
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int V = sc.nextInt();
		
		Graph graph = new Graph(N);
		int a;
		int b;
		for(int i=0;i<M;i++) {
			a = sc.nextInt();
			b = sc.nextInt();
			graph.addEdge(a, b);
		}
		sc.close();
		graph.dfs(V);
		System.out.println();
		graph.bfs(V);
	}
}

