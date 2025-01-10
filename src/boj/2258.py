import sys

input = sys.stdin.readline

n, m = map(int, input().split())

meat = [tuple(map(int, input().split())) for _ in range(n)]

meat.sort(key=lambda x: (x[1], -x[0]))
w_sum = 0
current_cost = 0
total_cost = 0
min_cost = 2147483647
check = False
for w, p in meat:
    w_sum += w
    if current_cost == p:
        total_cost += current_cost
    else:
        current_cost = p
        total_cost = p
    if w_sum >= m:
        min_cost = min(min_cost, total_cost)
        check = True

if check:
    print(min_cost)
else:
    print(-1)
