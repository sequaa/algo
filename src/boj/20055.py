import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

a = list(map(int, input().split()))

robot_pos = deque([])
cnt = 0

while True:
    cnt += 1

    temp = a[-1]
    for i in range(2*n-1, 0, -1):
        a[i] = a[i-1]
    a[0] = temp

    for i in range(len(robot_pos)):
        robot_pos[i] += 1

    if robot_pos and robot_pos[0] == n-1:
        robot_pos.popleft()

    for i in range(len(robot_pos)):
        if robot_pos[i]+1 not in robot_pos and a[robot_pos[i]+1] > 0:
            robot_pos[i] += 1
            a[robot_pos[i]] -= 1

    if robot_pos and robot_pos[0] == n-1:
        robot_pos.popleft()

    if a[0] != 0:
        robot_pos.append(0)
        a[0] -= 1

    zero_cnt = 0
    for point in a:
        if point <= 0:
            zero_cnt += 1

    if zero_cnt >= k:
        break

print(cnt)