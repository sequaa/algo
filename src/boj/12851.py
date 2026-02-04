import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque([(n, 0)])
visited = [-1] * 100001
visited[n] = 0
count = [0] * 100001
count[n] = 1

while queue:
    current, time = queue.popleft()

    for next in [current-1, current+1, current*2]:
        if 0 <= next <= 100000:
            if visited[next] == -1:
                visited[next] = time + 1
                count[next] = count[current]
                queue.append((next, time+1))
            elif visited[next] == time + 1:
                count[next] += count[current]


print(visited[k])
print(count[k])
