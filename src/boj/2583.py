# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# m, n, k = map(int, input().split())
#
# board = [[0] * (m+1) for _ in range(n+1)]
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(x1, x2+1):
#         for j in range(y1, y2+1):
#             board[i][j] = 1
#
# new_board = [[0] * m for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# for i in range(n):
#     for j in range(m):
#         if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
#             new_board[i][j] = 1
#
#
# def bfs(a, b):
#     visited[a][b] = True
#     cnt = 1
#     queue = deque([(a, b)])
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0 <= nx < n and 0 <= ny < m and not new_board[nx][ny] and not visited[nx][ny]:
#                 queue.append((nx, ny))
#                 visited[nx][ny] = True
#                 cnt += 1
#
#     return cnt
#
#
# area = []
# for i in range(n):
#     for j in range(m):
#         if new_board[i][j] == 0 and not visited[i][j]:
#             area.append(bfs(i, j))
#
# area.sort()
# print(len(area))
# for a in area:
#     print(a, end=' ')
#

import sys
from collections import deque

input = sys.stdin.readline

# 입력 처리
M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]  # M x N 격자 초기화

# 직사각형 그리기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[M - y - 1][x] = 1  # y축이 반대 방향으로 설정

# BFS로 영역 탐색
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    board[start_y][start_x] = 1  # 방문 처리
    area_size = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 이동
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and board[ny][nx] == 0:  # 범위 체크 및 방문 여부
                board[ny][nx] = 1  # 방문 처리
                queue.append((nx, ny))
                area_size += 1

    return area_size

# 남은 영역 탐색
areas = []
for y in range(M):
    for x in range(N):
        if board[y][x] == 0:  # 빈 공간이면
            area_size = bfs(x, y)
            areas.append(area_size)

# 결과 출력
areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))
