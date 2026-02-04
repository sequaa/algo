import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

grid = [list(input().strip()) for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ji, fire = (0, 0), []

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'J':
            ji = (i, j)
        elif grid[i][j] == 'F':
            fire.append((i, j))

queue = deque()
# queue.append(('J', ji[0], ji[1], 0))
for f in fire:
    queue.append(('F', f[0], f[1], 0))
queue.append(('J', ji[0], ji[1], 0))

visited = [[False] * c for _ in range(r)]

while queue:
    sb, x, y, cnt = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            if sb == 'J':
                print(cnt+1)
                sys.exit(0)
            elif sb == 'F':
                continue

        if grid[nx][ny] == '.' and not visited[nx][ny] and sb == 'J':
            visited[nx][ny] = True
            queue.append(('J', nx, ny, cnt+1))

        if sb == 'F' and (grid[nx][ny] == '.' or grid[nx][ny] == 'J'):
            queue.append(('F', nx, ny, 0))
            grid[nx][ny] = 'F'

print('IMPOSSIBLE')
