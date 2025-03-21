import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

visited = [False] * 100001
start, end = 0, 0
cnt = 0

while start < n and end < n:
    if not visited[num[end]]:
        visited[num[end]] = True
        end += 1
        cnt += end - start
    else:
        visited[num[start]] = False
        start += 1

print(cnt)