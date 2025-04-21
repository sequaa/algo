import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
parents = [i for i in range(n+1)]


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root != y_root:
        parents[y_root] = x_root

for i in range(1,n+1):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            union(i, j+1)

plan = list(map(int, input().split()))

for p in range(1, m):
    if find(plan[p-1]) != find(plan[p]):
        print("NO")
        sys.exit()
print("YES")
