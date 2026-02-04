package boj;

import java.io.*;
import java.util.*;

public class N13913 {
    static class Node {
        int position;
        int time;
        
        Node(int position, int time) {
            this.position = position;
            this.time = time;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        
        if (n == k) {
            System.out.println(0);
            System.out.println(n);
            return;
        }
        
        int[] parent = new int[100001];
        Arrays.fill(parent, -1);
        Queue<Node> queue = new LinkedList<>();
        
        queue.offer(new Node(n, 0));
        parent[n] = n;  // 시작점은 자기 자신을 부모로
        
        while (!queue.isEmpty()) {
            Node current = queue.poll();
            
            // 목적지 도달
            if (current.position == k) {
                System.out.println(current.time);
                
                // 경로 역추적
                List<Integer> path = new ArrayList<>();
                int pos = k;
                while (pos != n) {
                    path.add(pos);
                    pos = parent[pos];
                }
                path.add(n);
                
                // 역순으로 출력
                Collections.reverse(path);
                for (int i = 0; i < path.size(); i++) {
                    if (i > 0) System.out.print(" ");
                    System.out.print(path.get(i));
                }
                System.out.println();
                return;
            }
            
            // 다음 위치들 계산
            int[] nextPositions = {
                current.position - 1,
                current.position + 1,
                current.position * 2
            };
            
            for (int next : nextPositions) {
                if (next < 0 || next > 100000) continue;
                if (parent[next] != -1) continue;  // 이미 방문
                
                parent[next] = current.position;  // 부모 노드 저장
                queue.offer(new Node(next, current.time + 1));
            }
        }
    }
}
