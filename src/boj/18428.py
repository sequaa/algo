import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

graph = [list(input().split()) for _ in range(n)]
pos = []
teacher = []
student = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))
        if graph[i][j] == 'S':
            student.append((i, j))
        pos.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def check(a, b, c):
    for t in teacher:
        x, y = t[0], t[1]
        for i in range(4):
            for j in range(1, n):
                nx = x + j*dx[i]
                ny = y + j*dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in [a, b, c]:
                    break
                if (nx, ny) in student:
                    return False
    return True


result = 'NO'
total_cnt, pass_cnt = 0, 0
for a, b, c in combinations(pos, 3):
    total_cnt += 1
    if graph[a[0]][a[1]] != 'X' or graph[b[0]][b[1]] != 'X' or graph[c[0]][c[1]] != 'X':
        pass_cnt += 1
        continue
    if check(a, b, c):
        result = 'YES'
        break

print(result)
