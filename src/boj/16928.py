import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
snake = {}
ladder = {}
snake_key = set()
ladder_key = set()
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
    ladder_key.add(a)
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b
    snake_key.add(a)

min_cnt = float('inf')
queue = deque([(1, 0)])
visited = set()

while queue:
    start, cnt = queue.popleft()

    if start in ladder_key:
        start = ladder[start]

    elif start in snake_key:
        start = snake[start]

    visited.add(start)

    if start == 100:
        min_cnt = min(min_cnt, cnt)
        break

    if cnt >= min_cnt:
        continue

    for i in range(1, 7):
        if start+i <= 100 and start+i not in visited:
            queue.append((start+i, cnt+1))

print(min_cnt)
