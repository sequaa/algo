import sys

input = sys.stdin.readline

n, m = map(int, input().split())
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


for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

