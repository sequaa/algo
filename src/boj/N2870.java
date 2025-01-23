package boj;

import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class N2870 {

    static int N;
    static List<BigInteger> list = new ArrayList<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            getNum(str);
        }

        Collections.sort(list);
        StringBuilder sb = new StringBuilder();
        for (BigInteger i: list) {
            sb.append(i).append("\n");
        }
        System.out.println(sb.toString());
    }

    private static void getNum(String str) {
        String temp = "";

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (Character.isDigit(c)) {
                temp += c;
            }
            else {
                if (temp != "") {
                    list.add(new BigInteger(temp));
                    temp = "";
                }
            }
        }

        if (temp != "") {
            list.add(new BigInteger(temp));
        }
    }
}
