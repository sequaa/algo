import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_len = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = set()
            visited.add((i, j))
            queue = deque([(i, j, 0)])

            while queue:
                x, y, cnt = queue.popleft()
                max_len = max(max_len, cnt)
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and graph[nx][ny] == 'L':
                        queue.append((nx, ny, cnt+1))
                        visited.add((nx, ny))

print(max_len)