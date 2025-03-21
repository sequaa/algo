import sys

input = sys.stdin.readline

n = int(input())

part = []
for _ in range(n):
    x, y = map(int, input().split())
    part.append((x, y))

part.sort()

lines = []
for x, y in part:
    if not lines or lines[-1][1] < x:
        lines.append((x, y))
    else:
        lines[-1] = (lines[-1][0], max(lines[-1][1], y))

result = 0

for line in lines:
    result += line[1] - line[0]

print(result)