package boj;

import java.io.*;
import java.util.*;

public class N4179 {

    static int R, C;
    static char[][] grid;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static Queue<Node> queue = new LinkedList<>();

    static class Node {
        char type;
        int a, b, cnt;

        public Node(char type, int a, int b, int cnt) {
            this.type = type;
            this.a = a;
            this.b = b;
            this.cnt = cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        grid = new char[R][C];
        Node ji = null;

        for (int i = 0; i < R; i++) {
            String temp = br.readLine();
            for (int j = 0; j < C; j++) {
                grid[i][j] = temp.charAt(j);
                if (grid[i][j] == 'J') {
                    ji = new Node('J', i, j, 0);
                } else if (grid[i][j] == 'F') {
                    queue.offer(new Node('F', i, j, 0));
                }
            }
        }

        queue.offer(ji);
        bfs();
        System.out.println("IMPOSSIBLE");
    }

    static void bfs() {
        while (!queue.isEmpty()) {
            Node node = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = node.a + dx[i];
                int ny = node.b + dy[i];

                if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
                    if (node.type == 'J') {
                        System.out.println(node.cnt+1);
                        System.exit(0);
                    }
                    continue;
                }

                if (grid[nx][ny] == '.' && node.type == 'J') {
                    grid[nx][ny] = 'J';
                    queue.offer(new Node('J', nx, ny, node.cnt+1));
                } else if (node.type == 'F') {
                    if (grid[nx][ny] == 'J' || grid[nx][ny] == '.') {
                        grid[nx][ny] = 'F';
                        queue.offer(new Node('F', nx, ny, node.cnt+1));
                    }
                }
            }
        }
    }
}
