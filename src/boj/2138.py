import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().strip()))
e = list(map(int, input().strip()))


def change(start, end):
    temp = start[:]
    cnt = 0

    for i in range(1, n):
        if temp[i-1] == end[i-1]:
            continue

        for j in range(i-1, i+2):
            if j < n:
                temp[j] = 1 - temp[j]
        cnt += 1

    if temp == end:
        return cnt
    else:
        return float('INF')


result = change(s, e)
s[0] = 1 - s[0]
s[1] = 1 - s[1]
result = min(result, change(s, e)+1)
if result != float('INF'):
    print(result)
else:
    print(-1)
