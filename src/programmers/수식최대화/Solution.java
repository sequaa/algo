package programmers.수식최대화;

import java.util.*;

public class Solution {

    private static final String[][] PRIORITIES = {
            {"+", "-", "*"}, {"+", "*", "-"}, {"-", "+", "*"},
            {"-", "*", "+"}, {"*", "+", "-"}, {"*", "-", "+"}
    };

    public long solution(String expression) {
        long answer = 0;

        List<Long> numbers = new ArrayList<>();
        List<String> ops = new ArrayList<>();

        StringBuilder sb = new StringBuilder();
        for (char c : expression.toCharArray()) {
            if (c == '+' || c == '-' || c == '*') {
                ops.add(String.valueOf(c));
                numbers.add(Long.parseLong(sb.toString()));
                sb.setLength(0);
            } else {
                sb.append(c);
            }
        }

        for (String[] priority : PRIORITIES) {
            List<Long> subNumbers = new ArrayList<>(numbers);
            List<String> subOps = new ArrayList<>(ops);

            for (String targetOp : priority) {
                for (int i = 0; i < subOps.size();) {
                    if (subOps.get(i).equals(targetOp)) {
                        long res = calc(subNumbers.remove(i), subNumbers.remove(i), targetOp);
                        subNumbers.add(i, res);
                        subOps.remove(i);
                    } else {
                        i++;
                    }
                }
            }
            answer = Math.max(answer, Math.abs(subNumbers.get(0)));
        }
        return answer;
    }

    private long calc(long n1, long n2, String op) {
        return switch (op) {
            case "+" -> n1 + n2;
            case "-" -> n1 - n2;
            case "*" -> n1 * n2;
            default -> 0;
        };
    }
}
