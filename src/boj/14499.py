import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

g = []
for _ in range(n):
    g.append(list(map(int, input().split())))

dice = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


def move_dice(d):
    if d == 1:
        temp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = temp
    elif d == 2:
        temp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = temp
    elif d == 3:
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = temp
    elif d == 4:
        temp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = temp


direction = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
move_list = list(map(int, input().split()))

for move in move_list:
    nx = x + direction[move][0]
    ny = y + direction[move][1]

    if 0 <= nx < n and 0 <= ny < m:
        move_dice(move)
        if g[nx][ny] == 0:
            g[nx][ny] = dice[3][1]
        else:
            dice[3][1] = g[nx][ny]
            g[nx][ny] = 0
        print(dice[1][1])
        x, y = nx, ny
