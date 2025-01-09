import sys
from collections import deque

input = sys.stdin.readline

field = [list(input().strip()) for _ in range(12)]
pop_list = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    global pop_list
    current_color = field[a][b]
    queue = deque([(a, b)])
    temp = [(a, b)]
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and field[nx][ny] == current_color and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                temp.append((nx, ny))

    if len(temp) >= 4:
        pop_list += temp


pop_cnt = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                bfs(i, j)

    if pop_list:
        while pop_list:
            i, j = pop_list.pop()
            field[i][j] = '.'
        pop_cnt += 1
    else:
        break

    for j in range(6):
        for _ in range(11):
            for i in range(11, 0, -1):
                if field[i][j] == '.':
                    field[i][j], field[i-1][j] = field[i-1][j], field[i][j]

print(pop_cnt)