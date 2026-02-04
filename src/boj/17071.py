import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    visited = [[-1, -1] for _ in range(500001)]

    queue = deque()
    queue.append(N)
    visited[N][0] = 0

    time = 0

    while True:
        if K > 500000:
            return -1

        if visited[K][time%2] != -1:
            return time

        for _ in range(len(queue)):
            current = queue.popleft()

            for next_pos in [current-1, current+1, current*2]:
                if 0 <= next_pos <= 500000:
                    next_parity = (time+1) % 2

                    if visited[next_pos][next_parity] == -1:
                        visited[next_pos][next_parity] = time + 1
                        queue.append(next_pos)

        time += 1
        K += time

print(solve())