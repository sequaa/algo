import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque([(a, b)])
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and farm[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        farm[j][i] = 1

    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)
