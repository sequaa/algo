import sys

input = sys.stdin.readline

n, m, l, k = map(int, input().split())

stars = []
for _ in range(k):
    a, b = map(int, input().split())
    stars.append((a, b))

max_tramp = 0
for x, _ in stars:
    for _, y in stars:
        cnt = 0
        for a, b in stars:
            if x <= a <= x+l and y <= b <= y+l:
                cnt += 1

        max_tramp = max(cnt, max_tramp)

print(k-max_tramp)
