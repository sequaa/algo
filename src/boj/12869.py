import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n = int(input())

scv = tuple(map(int, input().split()))
mtl = {0:9, 1:3, 2:1}

queue = deque()
visited = set()
visited.add(scv)
queue.append((scv,0))

while queue:
    current, cnt = queue.popleft()

    for p in permutations(range(n), n):
        next_scv = []
        for i in range(n):
            temp = current[i] - mtl[p[i]]
            if temp < 0:
                temp = 0
            next_scv.append(temp)

        if sum(next_scv) == 0:
            print(cnt+1)
            sys.exit(0)
        next_scv = tuple(next_scv)
        if next_scv in visited:
            continue
        visited.add(next_scv)
        queue.append((next_scv, cnt+1))
