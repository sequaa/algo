package boj;

import java.util.*;
import java.io.*;

public class N12869 {

    static int N;
    static int[] mtl = {9, 3, 1};
    static Set<String> visited = new HashSet<>();
    static Queue<State> queue = new LinkedList<>();

    static class State {
        int[] scv;
        int cnt;

        State(int[] scv, int cnt) {
            this.scv = scv.clone();
            this.cnt = cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        int[] scv = new int[N];
        for (int i = 0; i < N; i++) {
            scv[i] = Integer.parseInt(st.nextToken());
        }

        String state = Arrays.toString(scv);
        visited.add(state);
        queue.offer(new State(scv, 0));

        while (!queue.isEmpty()) {
            State current = queue.poll();
            generatePermutation(current, 0, new int[N]);

        }

    }

    static void generatePermutation(State current, int depth, int[] perm) {
        if (depth == N) {
            int[] nextScv = new int[N];
            for (int i =0; i < N; i++) {
                int temp = current.scv[i] - mtl[perm[i]];
                nextScv[i] = Math.max(0, temp);
            }

            boolean allDead = true;
            for (int i = 0; i < N; i++) {
                if (nextScv[i] > 0) {
                    allDead = false;
                    break;
                }
            }

            if (allDead) {
                System.out.println(current.cnt + 1);
                System.exit(0);
            }

            String nextState = Arrays.toString(nextScv);
            if (visited.contains(nextState)) {
                return;
            }

            visited.add(nextState);
            queue.offer(new State(nextScv, current.cnt + 1));
            return;
        }

        for (int i = 0; i < N; i++) {
            boolean used = false;
            for (int j = 0; j < depth; j++) {
                if (perm[j] == i) {
                    used = true;
                    break;
                }
            }
            if (!used) {
                perm[depth] = i;
                generatePermutation(current, depth + 1, perm);
            }
        }
    }
}
