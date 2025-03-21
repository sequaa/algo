import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]
dp[0][num[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if 0 <= j-num[i] <= 20:
            dp[i][j] += dp[i-1][j-num[i]]
        if 0 <= j+num[i] <= 20:
            dp[i][j] += dp[i-1][j+num[i]]

print(dp[n-2][num[-1]])
