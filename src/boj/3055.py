import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
check = False
start = ()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            queue.append((i, j, 'S', 0))
            start = (i, j)
            visited[i][j] = True
for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            queue.append((i, j, '*', 0))
            visited[i][j] = True


while queue:
    x, y, sym, cnt = queue.popleft()

    if sym == 'S':
        if board[x][y] == 'D':
            check = True
            print(cnt)
            break
        elif board[x][y] == '*':
            continue

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if sym == '*':
            if 0 <= nx < r and 0 <= ny < c and (board[nx][ny] == '.' or board[nx][ny] == 'S'):
                queue.append((nx, ny, '*', cnt))
                if (nx, ny) == start:
                    pass
                else:
                    board[nx][ny] = '*'
        elif sym == 'S':
            if 0 <= nx < r and 0 <= ny < c and (board[nx][ny] == '.' or board[nx][ny] == 'D'):
                queue.append((nx, ny, 'S', cnt+1))
                if board[nx][ny] == '.':
                    board[nx][ny] = 'S'

if not check:
    print('KAKTUS')
