from collections import deque

def solution(storage, requests):
    answer = 0
    n, m = len(storage)+2, len(storage[0])+2
    new_storage = [[0] * m for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            new_storage[i][j] = storage[i-1][j-1]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def bfs(a, b):
        new_storage[a][b] = 0
        queue = deque([(a, b)])

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if new_storage[nx][ny] == 1:
                    new_storage[nx][ny] = 0
                    queue.append((nx, ny))

    for request in requests:
        if len(request) == 2:
            for i in range(1, n-1):
                for j in range(1, m-1):
                    if new_storage[i][j] == request[0]:
                        new_storage[i][j] = 1

        else:
            for i in range(1, n-1):
                for j in range(1, m-1):
                    if new_storage[i][j] == request[0]:
                        for k in range(4):
                            ni, nj = i+dx[k], j+dy[k]
                            if new_storage[ni][nj] == 0:
                                new_storage[i][j] = 1
                                break

        for i in range(1, n-1):
            for j in range(1, m-1):
                if new_storage[i][j] == 1:
                    for k in range(4):
                        ni, nj = i+dx[k], j+dy[k]
                        if new_storage[ni][nj] == 0:
                            bfs(i, j)
    answer = (n-2) * (m-2)
    for i in range(1, n-1):
        for j in range(1, m-1):
            if new_storage[i][j] == 0 or new_storage[i][j] == 1:
                answer -= 1

    return answer
