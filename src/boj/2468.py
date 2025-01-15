import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
max_rain = 0
for i in range(n):
    for j in range(n):
        max_rain = max(max_rain, graph[i][j])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b, r):
    visited[a][b] = True
    queue = deque([(a, b)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > r:
                queue.append((nx, ny))
                visited[nx][ny] = True


max_cnt = 0
for rain in range(max_rain):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and not visited[i][j]:
                bfs(i, j, rain)
                cnt += 1
    max_cnt = max(cnt, max_cnt)

print(max_cnt)