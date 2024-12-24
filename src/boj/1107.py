import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
bb = []
bt = []
if m:
    bb = list(map(int, input().split()))

for i in range(10):
    if i not in bb:
        bt.append(i)

min_cnt = abs(n-100)

for i in range(1000001):
    num = str(i)

    check = True
    for j in num:
        if int(j) not in bt:
            check = False
            break

    if check:
        min_cnt = min(min_cnt, len(num)+abs(n - int(num)))

print(min_cnt)
