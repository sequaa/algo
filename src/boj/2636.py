import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [[False] * m for _ in range(n)]


def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and cheese[nx][ny] != 1:
                queue.append((nx, ny))
                visited[nx][ny] = True


day = 0
remain = 0
while True:
    visited = [[False] * m for _ in range(n)]
    bfs()
    check = False

    cnt = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                check = True
                cnt += 1
                for k in range(4):
                    ni = i+dx[k]
                    nj = j+dy[k]
                    if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] and cheese[ni][nj] != 1:
                        cheese[i][j] = 0
    if not check:
        break
    remain = cnt
    day += 1

print(day)
print(remain)
