package boj;

import java.util.*;
import java.io.*;

public class N16637 {

    static int N;
    static int result = (int) -Math.pow(2, 31);
    static char[] eq;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        eq = new char[N];

        String temp = br.readLine();
        for (int i = 0; i < N; i++) {
            eq[i] = temp.charAt(i);
        }

        dfs(eq[0] - '0', 0);
        System.out.println(result);
    }

    static int calculate(int a, char op, int b) {
        if (op == '+') {
            return a + b;
        } else if (op == '-') {
            return a - b;
        } else if (op == '*') {
            return a * b;
        }
        return 0;
    }

    static void dfs(int temp, int idx) {
        if (idx == N - 1) {
            result = Math.max(result, temp);
            return;
        }

        if (idx + 2 < N) {
            dfs(calculate(temp, eq[idx+1], eq[idx+2] - '0'), idx+2);
        }

        if (idx + 4 < N) {
            dfs(calculate(temp, eq[idx + 1], calculate(eq[idx + 2] - '0', eq[idx + 3], eq[idx + 4] - '0')), idx + 4);
        }
    }

}
