import sys

input = sys.stdin.readline

n = int(input())
buildings = list(map(int, input().split()))

max_cnt = 0

for i in range(n):
    cnt = 0
    current_left = float('INF')
    current_right = -float('INF')
    for j in range(i-1, -1, -1):
        angle = (buildings[i] - buildings[j]) / (i - j)
        if current_left > angle:
            cnt += 1
            current_left = angle
    for j in range(i+1, n):
        angle = (buildings[j] - buildings[i]) / (j - i)
        if current_right < angle:
            cnt += 1
            current_right = angle

    max_cnt = max(max_cnt, cnt)

print(max_cnt)
