import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

dx = [1, 0]
dy = [0, 1]

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        for k in range(2):
            ni, nj = i+dx[k]*board[i][j], j+dy[k]*board[i][j]
            if 0 <= ni < n and 0 <= nj < n:
                dp[ni][nj] += dp[i][j]

print(dp[n-1][n-1])
