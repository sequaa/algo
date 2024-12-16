import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]
robot = []
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if room[i][j] == -1:
            robot.append((i, j))
        if room[i][j] > 0:
            queue.append((i, j, room[i][j]))
for _ in range(t):

    while queue:
        r, c, v = queue.popleft()

        move_v = v//5
        cnt = 0
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in robot:
                cnt += 1
                room[nx][ny] += move_v
        room[r][c] -= move_v * cnt

    for i in range(robot[0][0]-1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(0, m-1):
        room[0][i] = room[0][i+1]
    for i in range(0, robot[0][0]):
        room[i][m-1] = room[i+1][m-1]
    for i in range(m-1, 1, -1):
        room[robot[0][0]][i] = room[robot[0][0]][i-1]
    room[robot[0][0]][1] = 0

    for i in range(robot[1][0]+1, n-1):
        room[i][0] = room[i+1][0]
    for i in range(0, m-1):
        room[n-1][i] = room[n-1][i+1]
    for i in range(n-1, robot[1][0], -1):
        room[i][m-1] = room[i-1][m-1]
    for i in range(m-1, 1, -1):
        room[robot[1][0]][i] = room[robot[1][0]][i-1]
    room[robot[1][0]][1] = 0

    for i in range(n):
        for j in range(m):
            if room[i][j] > 0:
                queue.append((i, j, room[i][j]))

result = 0
for i in range(n):
    for j in range(m):
        if room[i][j] > 0:
            result += room[i][j]

print(result)