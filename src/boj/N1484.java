package boj;

import java.io.*;
import java.util.*;

public class N1484 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int start = 1, end = 2;

        StringBuilder sb = new StringBuilder();

        while (true) {
            int temp = end*end - start*start;
            if (temp > n) {
                if (end - start == 1) {
                    break;
                }
                start += 1;
            } else if (temp < n) {
                end += 1;
            } else {
                sb.append(end).append("\n");
                end += 1;
            }
        }

        if (sb.length() == 0) {
            System.out.println(-1);
        } else {
            System.out.println(sb);
        }

    }
}
