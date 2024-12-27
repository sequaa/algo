import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

outer = set()
outer.add((0, 0))

queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in outer and not graph[nx][ny]:
            outer.add((nx, ny))
            queue.append((nx, ny))

day = 0
while sum(map(sum, graph)):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if (nx, ny) in outer:
                        cnt += 1
                if cnt >= 2:
                    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        outer.add((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) not in outer and not graph[nx][ny]:
                outer.add((nx, ny))
                queue.append((nx, ny))

    day += 1

print(day)