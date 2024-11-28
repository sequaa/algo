import sys
import heapq

input = sys.stdin.readline

n = int(input())

time = [list(map(int,input().split())) for _ in range(n)]
time.sort()

room = [0]

for t in time:
    if t[0] >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room, t[1])
    else:
        heapq.heappush(room, t[1])

print(len(room))