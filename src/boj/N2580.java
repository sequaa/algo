package boj;

import java.util.*;
import java.io.*;

public class N2580 {

    static int[][] sudoku = new int[9][9];
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int i = 0; i < 9; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                sudoku[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solve(0, 0);

    }

    public static void solve(int row, int col) {

        if (row == 9) {
            solve(0, col+1);
            return;
        }

        if (col == 9) {
            printSudoku();
            System.exit(0);
        }

        if (sudoku[row][col] != 0) {
            solve(row+1, col);
            return;
        }

        for (int num = 1; num <= 9; num++) {
            if (isValid(row, col, num)) {
                sudoku[row][col] = num;
                solve(row+1, col);
                sudoku[row][col] = 0;
            }
        }
    }

    public static boolean isValid(int row, int col, int num) {
        for (int i = 0; i < 9; i++) {
            if (sudoku[row][i] == num || sudoku[i][col] == num) return false;
        }

        int x = (row/3)*3;
        int y = (col/3)*3;
        for (int i = x; i < x+3; i++) {
            for (int j = y; j < y+3; j++) {
                if (sudoku[i][j] == num) return false;
            }
        }
        return true;
    }

    public static void printSudoku() {
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                sb.append(sudoku[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
