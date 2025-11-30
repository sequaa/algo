package boj;

import java.util.*;
import java.io.*;

public class N17071 {

    static final int MAX = 500000;
    static int N, K;
    static int time = 0;
    static int[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        visited = new int[MAX+1][2];
        for (int i = 0; i <= MAX; i++) {
            Arrays.fill(visited[i], -1);
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(N);
        visited[N][0] = 0;

        while (true) {

            if (K > MAX) {
                System.out.println(-1);
                return;
            }

            if (visited[K][time%2] != -1) {
                System.out.println(time);
                return;
            }

            int size = queue.size();
            for  (int i = 0; i < size; i++) {
                int current = queue.poll();

                int[] nextPositions = {current-1, current+1, current*2};

                for (int nextPos :  nextPositions) {

                    if (nextPos < 0 || nextPos > MAX) continue;

                    int nextParity = (time+1) % 2;

                    if (visited[nextPos][nextParity] == -1) {
                        visited[nextPos][nextParity] = time + 1;
                        queue.offer(nextPos);
                    }
                }
            }
            time++;
            K += time;
        }
    }
}
