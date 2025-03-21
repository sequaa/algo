import sys

input = sys.stdin.readline

m, n, l = map(int, input().split())

shot_list = list(map(int, input().split()))
shot_list.sort()

cnt = 0


def b_search(t):
    start, end = 0, m-1

    while start <= end:
        mid = (start + end) // 2

        if shot_list[mid] < t:
            start = mid+1
        elif shot_list[mid] > t:
            end = mid-1
        else:
            return shot_list[mid]

    closest = None

    if start < m:
        closest = shot_list[start]
    if end >= 0:
        if closest is None or abs(shot_list[end] - t) < abs(closest - t):
            closest = shot_list[end]
    return closest


for _ in range(n):
    x, y = map(int, input().split())
    if m > 1:
        temp = b_search(x)
    else:
        temp = shot_list[0]
    if abs(temp-x)+y <= l:
        cnt += 1

print(cnt)