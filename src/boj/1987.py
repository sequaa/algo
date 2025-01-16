import sys

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(input().strip()) for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

max_cnt = 0
route = set()


def dfs(a, b, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for i in range(4):
        nx, ny = a+dx[i], b+dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in route:
            route.add(board[nx][ny])
            dfs(nx, ny, cnt+1)
            route.remove(board[nx][ny])


route.add(board[0][0])
dfs(0, 0, 1)
print(max_cnt)