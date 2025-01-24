import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                queue.append((i, j, '@', 0))
                break

    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                queue.append((i, j, '*', 0))

    check = False
    while queue:
        x, y, sym, cnt = queue.popleft()
        if x == h and y == w:
            print(cnt)
            check = True
            break
        elif sym == '@' and building[x][y] == '*':
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if sym == '@':
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    queue.append((h, w, '@', cnt+1))
                elif 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.':
                    queue.append((nx, ny, '@', cnt+1))
                    building[nx][ny] = '@'
            elif sym == '*':
                if 0 <= nx < h and 0 <= ny < w and (building[nx][ny] == '.' or building[nx][ny] == '@'):
                    queue.append((nx, ny, '*', cnt))
                    building[nx][ny] = '*'

    if not check:
        print('IMPOSSIBLE')

