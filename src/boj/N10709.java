package boj;

import java.io.*;
import java.util.*;

public class N10709 {
    static int h, w;
    static int[][] result;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        result = new int[h][w];

        for (int i = 0; i < h; i++) {
            String temp = br.readLine();
            for (int j = 0; j < w; j++) {
                if (temp.charAt(j) == 'c') {
                    result[i][j] = 0;
                } else {
                    result[i][j] = -1;
                }
            }
        }

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (result[i][j] == 0) {
                    for (int k = j+1; k < w; k++) {
                        if (result[i][k] != 0) {
                            result[i][k] = result[i][k-1] + 1;
                        }
                    }
                }
            }
        }

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                bw.write(result[i][j] + " ");
            }
            bw.write("\n");
        }

        bw.flush();
    }
}
