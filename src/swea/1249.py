from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T+1):
    n = int(input())
    graph = []
    for _ in range(n):
        l = input().rstrip()
        temp = []
        for s in l:
            temp.append(int(s))
        graph.append(temp)
    visited = [[999999999 for _ in range(n)] for _ in range(n)]
    visited[0][0] = graph[0][0]

    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = visited[x][y] + graph[nx][ny]

                if cost < visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = cost

    print("#{} {}".format(test_case, visited[n-1][n-1]))
