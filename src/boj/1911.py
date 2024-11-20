import sys

input = sys.stdin.readline

n, L = map(int, input().split())

water = [list(map(int, input().split())) for _ in range(n)]

water.sort(key=lambda x: x[0])

cnt = 0
current_idx = 0

for w in water:
    a, b = w[0], w[1]

    for i in range(a, b):
        if i > current_idx:
            cnt += 1
            current_idx = i + L - 1

print(cnt)
