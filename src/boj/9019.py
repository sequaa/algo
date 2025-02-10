import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input_str, target = map(int, input().split())
    visited = set()

    queue = deque([(input_str, '')])
    visited.add(input_str)

    while queue:
        current, commands = queue.popleft()

        if current == target:
            print(commands)
            break

        d = (current * 2) % 10000
        if d not in visited:
            visited.add(d)
            queue.append((d, commands + 'D'))

        s = (current - 1) if current > 0 else 9999
        if s not in visited:
            visited.add(s)
            queue.append((s, commands + 'S'))

        l = (current % 1000) * 10 + (current // 1000)
        if l not in visited:
            visited.add(l)
            queue.append((l, commands + 'L'))

        r = (current % 10) * 1000 + (current // 10)
        if r not in visited:
            visited.add(r)
            queue.append((r, commands + 'R'))