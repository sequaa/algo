package boj;

import java.util.*;
import java.io.*;

public class N3474 {
    static int t;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int count = 0;
            int target = 5;

            while (n >= target) {
                count += n / target;
                target *= 5;
            }
            System.out.println(count);
        }

    }
}
