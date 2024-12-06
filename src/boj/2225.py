import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (n+1) for _ in range(k)]

for i in range(n+1):
    dp[0][i] = 1

for i in range(k):
    dp[i][0] = 1


for x in range(1, k):
    for y in range(1, n+1):
        dp[x][y] = dp[x][y-1] + dp[x-1][y]

print(dp[k-1][n] % 1000000000)
