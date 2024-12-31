import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n = int(input())

min_heap = []
max_heap = []
solve = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(min_heap, (b, a))
    heapq.heappush(max_heap, (-b, -a))

m = int(input())
for _ in range(m):
    commend = input().split()

    if commend[0] == 'add':
        a, b = int(commend[1]), int(commend[2])
        heapq.heappush(min_heap, (b, a))
        heapq.heappush(max_heap, (-b, -a))

    elif commend[0] == 'solved':
        solve[int(commend[1])] += 1

    else:
        if commend[1] == '1':
            while solve[-max_heap[0][1]] != 0:
                solve[-max_heap[0][1]] -= 1
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while solve[min_heap[0][1]] != 0:
                solve[min_heap[0][1]] -= 1
                heapq.heappop(min_heap)
            print(min_heap[0][1])
