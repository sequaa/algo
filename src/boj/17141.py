import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

lab = []
emt = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
wall_cnt = 0

for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(n):
        if lab[i][j] == 2:
            emt.append((i, j))
        elif lab[i][j] == 1:
            wall_cnt += 1


min_time = float('inf')
virus = list(combinations(emt, m))
check = False

for v in virus:
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    total_time = 0
    cnt = 0
    for a, b in v:
        visited[a][b] = True
        queue.append((a, b, 0))

    while queue:
        x, y, time = queue.popleft()
        cnt += 1
        total_time = max(total_time, time)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and lab[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, time+1))

    if wall_cnt + cnt == n**2:
        min_time = min(min_time, total_time)

if min_time == float('inf'):
    print(-1)
else:
    print(min_time)