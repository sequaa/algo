import sys

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
working = set()
for _ in range(k):
    a, b, c, d = map(int, input().split())
    working.add((a, b, c, d))
    working.add((c, d, a, b))

dp = [[0] * (m+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(n+1):
    for j in range(m+1):
        if i == 0 and j == 0:
            continue
        if (i, j-1, i, j) not in working:
            dp[i][j] += dp[i][j-1]
        if (i-1, j, i, j) not in working:
            dp[i][j] += dp[i-1][j]

print(dp[n][m])

