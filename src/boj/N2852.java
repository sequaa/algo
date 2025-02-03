package boj;

import java.util.*;
import java.io.*;

public class N2852 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int team1Time = 0, team2Time = 0, lastLeadTime = 0, lastScore1 = 0, lastScore2 = 0;

        int[][] scores = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int team = Integer.parseInt(st.nextToken());
            String[] time = st.nextToken().split(":");
            int minute = Integer.parseInt(time[0]);
            int second = Integer.parseInt(time[1]);
            scores[i][0] = team;
            scores[i][1] = minute * 60 + second;
        }

        for (int i = 0; i < n; i++) {
            int currentTeam = scores[i][0];
            int currentTime = scores[i][1];

            if (i > 0) {
                int duration = currentTime - lastLeadTime;
                if (lastScore1 > lastScore2) {
                    team1Time += duration;
                } else if (lastScore1 < lastScore2) {
                    team2Time += duration;
                }
            }

            if (currentTeam == 1) lastScore1++;
            else lastScore2++;

            lastLeadTime = currentTime;
        }

        int totalTime = 48 * 60;
        if (lastScore1 > lastScore2) team1Time += totalTime - lastLeadTime;
        else if (lastScore1 < lastScore2) team2Time += totalTime - lastLeadTime;

        System.out.println(formatTime(team1Time));
        System.out.println(formatTime(team2Time));
    }

    private static String formatTime(int time) {
        int minute = time / 60;
        int second = time % 60;
        return String.format("%02d:%02d", minute, second);
    }
}
