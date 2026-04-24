package programmers.카펫;

class Solution {
    public int[] solution(int brown, int yellow) {
        int n = 3;
        while (true) {
            for (int m=1; m <= n; m++) {
                if ((n * m) >= (brown + yellow)) {
                    if ((n * m) == (brown + yellow)) {
                        if ((n-2) * (m-2) == yellow) {
                            return new int[]{n,m};
                        }
                    }
                }
            }
            n += 1;
        }
    }
}