import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num = [int(input()) for _ in range(n)]

num.sort()
result = 2000000001
start, end = 0, 0
while start < n and end < n:
    temp = num[end] - num[start]
    if temp < m:
        if end == n-1:
            break
        else:
            end += 1

    else:
        result = min(temp, result)
        start += 1

print(result)