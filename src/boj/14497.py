import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    answer = 0
    classroom = [list(input().strip()) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while True:
        answer += 1
        visited = [[False] * M for _ in range(N)]
        queue = deque([(x1-1, y1-1)])

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if classroom[nx][ny] == '#':
                        return answer

                    if classroom[nx][ny] == '0':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    elif classroom[nx][ny] == '1':
                        visited[nx][ny] = True
                        classroom[nx][ny] = '0'


print(solve())