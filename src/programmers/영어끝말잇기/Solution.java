package programmers.영어끝말잇기;

import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        Set<String> usedWords = new HashSet<>();
        char lastChar = words[0].charAt(0);

        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if (usedWords.contains(word) || word.charAt(0) != lastChar) {
                return new int[]{(i%n)+1, (i/n)+1};
            }
            usedWords.add(word);
            lastChar = word.charAt(word.length() - 1);
        }

        return new int[]{0, 0};
    }
}