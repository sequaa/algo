import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

iceberg = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if iceberg[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                else:
                    zero[x][y] += 1


year = 0
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    zero = [[0] * m for _ in range(n)]
    all_zero = True
    cnt = 0
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] and not visited[i][j]:
                cnt += 1
                if cnt > 1:
                    break
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            iceberg[i][j] = max(0, iceberg[i][j] - zero[i][j])
            if iceberg[i][j]:
                all_zero = False

    if all_zero or cnt > 1:
        break

    year += 1

if not all_zero:
    print(year)
else:
    print(0)
