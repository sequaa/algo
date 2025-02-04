import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()


def bfs():

    while queue:
        g, e, f = queue.popleft()
        for i in range(6):
            ne = e + dx[i]
            nf = f + dy[i]
            ng = g + dz[i]
            if 0 <= ne < n and 0 <= nf < m and 0 <= ng < h and tomato[ng][ne][nf] == 0:
                queue.append((ng, ne, nf))
                tomato[ng][ne][nf] = tomato[g][e][f] + 1


for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 1:
                queue.append((z, x, y))

bfs()

max_day = 0
is_in_zero = False

for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 0:
                is_in_zero = True
            max_day = max(max_day, tomato[z][x][y])

if not is_in_zero:
    print(max_day-1)
else:
    print(-1)
