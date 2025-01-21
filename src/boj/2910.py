import sys

input = sys.stdin.readline

n, c = map(int,input().split())

s = list(map(int,input().split()))

d = {}
idx = 1

for i in s:
    if i in d:
        d[i][0] += 1
    else:
        d[i] = [1, idx]
        idx += 1

numbers = [(i, j) for i, j in d.items()]

numbers.sort(key=lambda x: (-x[1][0],x[1][1]))
res = []
for i, j in numbers:
    res += [i]*j[0]
print(*res)