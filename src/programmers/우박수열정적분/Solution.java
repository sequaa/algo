package programmers.우박수열정적분;

import java.util.*;

class Solution {

    static int n;
    static ArrayList<Integer> ubakSequence = new ArrayList<>();
    static ArrayList<Double> answer = new ArrayList<>();

    public double[] solution(int k, int[][] ranges) {

        ubakSequence.add(k);
        while (k > 1) {
            if (k % 2 == 0) {
                k /= 2;
            } else {
                k = 3*k + 1;
            }
            ubakSequence.add(k);
        }
        n = ubakSequence.size() - 1;

        for (int[] range : ranges) {
            int a = range[0];
            int b = n + range[1];
            if (a > b) {
                answer.add(-1.0);
            } else if (a == b) {
                answer.add(0.0);
            } else {
                double temp = 0.0;
                for (int i = a; i < b; i++) {
                    temp += (ubakSequence.get(i) + ubakSequence.get(i+1)) / 2.0;
                }
                answer.add(temp);
            }


        }
        return answer.stream().mapToDouble(Double::doubleValue).toArray();
    }
}