package boj;

import java.io.*;
import java.util.*;

public class N14620 {

    static int N, minCost = 30001;
    static int[][] ground;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        visited = new boolean[N][N];
        ground = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                ground[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0,0);
        System.out.println(minCost);

    }

    public static boolean canPlant(int x, int y) {
        if (visited[x][y]) return false;
        for (int i = 0; i < 4; i++) {
            if (visited[x+dx[i]][y+dy[i]]) return false;
        }
        return true;
    }

    public static int plant(int x, int y, boolean isPlanting) {
        int cost = ground[x][y];
        visited[x][y] = isPlanting;
        for (int i = 0; i < 4; i++) {
            cost += ground[x + dx[i]][y + dy[i]];
            visited[x + dx[i]][y + dy[i]] = isPlanting;
        }

        return cost;
    }

    public static void dfs(int count, int currentCost) {
        if (currentCost >= minCost) {
            return;
        }

        if (count == 3) {
            minCost = Math.min(minCost, currentCost);
            return;
        }

        for (int i = 1; i < N-1; i++) {
            for (int j = 1; j < N-1; j++) {
                if (canPlant(i, j)) {
                    int cost = plant(i, j, true);
                    dfs(count+1, currentCost + cost);
                    plant(i, j, false);
                }
            }
        }
    }
}
