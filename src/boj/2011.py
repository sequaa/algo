import sys

input = sys.stdin.readline

n = input().rstrip()

if n[0] == '0':
    print(0)
    sys.exit()

len_n = len(n)
dp = [0] * (len_n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, len_n+1):
    temp1 = int(n[i-1:i])
    temp2 = int(n[i-2:i])

    if 1 <= temp1 <= 9:
        dp[i] += dp[i-1]

    if 10 <= temp2 <= 26:
        dp[i] += dp[i-2]

    dp[i] %= 1000000

print(dp[len_n])
