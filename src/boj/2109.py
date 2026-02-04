import sys, heapq

input = sys.stdin.readline

n = int(input())
pay = []

for _ in range(n):
    p, d = map(int, input().split())
    pay.append((p, d))

pay.sort(key=lambda x: x[1])

hq = []
for p, d in pay:
    heapq.heappush(hq, p)
    if len(hq) > d:
        heapq.heappop(hq)

print(sum(hq))