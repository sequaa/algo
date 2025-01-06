import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[False] * w for _ in range(h)] for _ in range(k+1)]

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
h_direction = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

queue = deque([(0, 0, k, 0)])
visited[k][0][0] = True

min_cnt = -1
while queue:
    x, y, k_cnt, cnt = queue.popleft()
    if (x, y) == (h-1, w-1):
        min_cnt = cnt
        break

    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and not visited[k_cnt][nx][ny]:
            queue.append((nx, ny, k_cnt, cnt+1))
            visited[k_cnt][nx][ny] = True

    if k_cnt > 0:
        for hd in h_direction:
            nx = x + hd[0]
            ny = y + hd[1]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != 1 and not visited[k_cnt-1][nx][ny]:
                queue.append((nx, ny, k_cnt-1, cnt+1))
                visited[k_cnt-1][nx][ny] = True

print(min_cnt)
