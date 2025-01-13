import sys
sys.setrecursionlimit(100000000)

input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
way = [[-1 for _ in range(n)] for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(a, b):
    if a == m-1 and b == n-1:
        return 1

    if way[a][b] != -1:
        return way[a][b]

    total_cnt = 0
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0 <= nx < m and 0 <= ny < n and graph[a][b] > graph[nx][ny]:
            total_cnt += dfs(nx, ny)

    way[a][b] = total_cnt
    return total_cnt


result = dfs(0, 0)
print(result)

# dp 풀이

# dp = [[0] * n for _ in range(m)]
# dp[0][0] = 1
#
# points = [(i, j) for i in range(m) for j in range(n)]
# points.sort(key=lambda x: graph[x[0]][x[1]], reverse=True)
#
# for x, y in points:
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
#             dp[nx][ny] += dp[x][y]
#
# print(dp[m-1][n-1])
