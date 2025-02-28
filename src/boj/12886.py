import sys
from collections import deque

input = sys.stdin.readline

a, b, c = map(int, input().split())
visited = set()
visited.add((a, b, c))
check = False

queue = deque([(a, b, c)])
while queue:
    temp = list(queue.popleft())
    temp.sort()
    x, y, z = temp[0], temp[1], temp[2]
    if x == y == z:
        check = True
        print(1)
        break

    if (x*2, y, z-x) not in visited:
        queue.append((x*2, y, z-x))
        visited.add((x*2, y, z-x))

    if (x*2, y-x, z) not in visited:
        queue.append((x*2, y-x, z))
        visited.add((x*2, y-x, z))

    if (x, y*2, z-y) not in visited:
        queue.append((x, y*2, z-y))
        visited.add((x, y*2, z-y))

if not check:
    print(0)
