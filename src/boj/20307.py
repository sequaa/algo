import sys

input = sys.stdin.readline

n = int(input())
events = [tuple(map(int, input().split())) for _ in range(n)]

year = [0] * 366

for a, b in events:
    for i in range(a, b+1):
        year[i] += 1

result = 0
r, c = 0, 0
for i in year:
    if i != 0:
        c = max(c, i)
        r += 1
    else:
        result += r * c
        r, c = 0, 0
result += r * c
print(result)
