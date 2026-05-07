package programmers.단어변환;

import java.util.*;

class Solution {

    static class Node {
        String word;
        int count;

        Node(String word, int count) {
            this.word = word;
            this.count = count;
        }
    }

    public int solution(String begin, String target, String[] words) {

        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(begin, 0));

        Set<String> visited = new HashSet<>();

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            if (current.word.equals(target)) {
                return current.count;
            }

            for (String word : words) {
                if(!visited.contains(word) && isAvailable(current.word, word)) {
                    visited.add(word);
                    queue.add(new Node(word, current.count+1));
                }
            }
        }
        return 0;
    }

    private boolean isAvailable(String start, String end) {
        int check = 0;
        for (int i = 0; i < start.length(); i++) {
            if (start.charAt(i) != end.charAt(i)) {
                check++;
            }
            if (check > 1) return false;
        }
        return true;
    }
}