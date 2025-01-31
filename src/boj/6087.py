import sys
from collections import deque

input = sys.stdin.readline

w, h = map(int, input().split())
board = [list(input().strip()) for _ in range(h)]
points = []
visited = [[[float('inf')] * w for _ in range(h)] for _ in range(4)]
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            points.append((i, j))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

queue = deque()
for i in range(4):
    nx, ny = points[0][0] + directions[i][0], points[0][1] + directions[i][1]
    if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '*':
        queue.append((i, nx, ny))
        visited[i][nx][ny] = 0

while queue:
    direction, x, y = queue.popleft()

    for i in range(4):
        nx, ny = x+directions[i][0], y+directions[i][1]

        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '*':
            cnt = visited[direction][x][y]
            if direction == 0 or direction == 2:
                if i == 1 or i == 3:
                    cnt += 1
            else:
                if i == 0 or i == 2:
                    cnt += 1

            if visited[i][nx][ny] == float('inf'):
                visited[i][nx][ny] = cnt
                queue.append((i, nx, ny))
            else:
                if visited[i][nx][ny] > cnt:
                    visited[i][nx][ny] = cnt
                    queue.append((i, nx, ny))

min_cnt = 99999999
for i in range(4):
    min_cnt = min(min_cnt, visited[i][points[1][0]][points[1][1]])

print(min_cnt)