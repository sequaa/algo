import sys

input = sys.stdin.readline

n = int(input())

line = [tuple(map(int, input().split())) for _ in range(n)]
line.sort()
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if line[j][1] < line[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
