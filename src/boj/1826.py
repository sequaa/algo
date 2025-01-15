import sys
import heapq

input = sys.stdin.readline

n = int(input())

stations = []
for _ in range(n):
    a, b = map(int, input().split())
    stations.append((a, b))
stations.sort()

town, current_oil = map(int, input().split())
cnt = 0
pos = 0
oil_list = []
while current_oil < town:
    while pos < len(stations) and stations[pos][0] <= current_oil:
        heapq.heappush(oil_list, -stations[pos][1])
        pos += 1

    if not oil_list:
        cnt = -1
        break

    current_oil -= heapq.heappop(oil_list)
    cnt += 1

print(cnt)
