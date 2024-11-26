import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]

print(dp[k])


# def dfs(idx, current_money):
#     global cnt
#     if current_money == 0:
#         cnt += 1
#         return
#     elif current_money < 0 or idx == n:
#         return
#
#     dfs(idx, current_money - coin[idx])
#     dfs(idx + 1, current_money)
#
#
# cnt = 0
# dfs(0, k)
#
# print(cnt)
