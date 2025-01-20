import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
temp = [list(map(int, input().strip())) for _ in range(n)]
board = [temp for _ in range(2)]
visited = [[[False] * m for _ in range(n)] for _ in range(2)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

min_cnt = -1
queue = deque([(0, 0, 0, 0)])
visited[0][0][0] = True
while queue:
    bk, x, y, cnt = queue.popleft()
    cnt += 1

    if x == n-1 and y == m-1:
        min_cnt = cnt
        break

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[bk][nx][ny] != 1 and not visited[bk][nx][ny]:
            queue.append((bk, nx, ny, cnt))
            visited[bk][nx][ny] = True
        if bk == 0:
            if 0 <= nx < n and 0 <= ny < m and board[bk][nx][ny] == 1 and not visited[bk][nx][ny]:
                queue.append((1, nx, ny, cnt))
                visited[bk][nx][ny] = True

print(min_cnt)