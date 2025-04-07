import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())

tree = defaultdict(list)

for _ in range(n-1):
    u, v, d = map(int, input().split())
    tree[u].append((v, d))
    tree[v].append((u, d))


def bfs(start, target):
    queue = deque([(start, 0)])

    visited = {start}
    while queue:
        node, current_d = queue.popleft()

        if node == target:
            return current_d

        for neighbor, next_d in tree[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, current_d + next_d))


for _ in range(m):
    a, b = map(int, input().split())
    distance = bfs(a, b)
    print(distance)