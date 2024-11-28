import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

result = set()
visited = set()


def dfs(a, b, c):
    if (a, b, c) in visited:
        return

    if a == 0:
        result.add(c)
    visited.add((a, b, c))

    if a != 0:
        if a > B - b:
            dfs(a-B+b, B, c)
        else:
            dfs(0, a+b, c)
        if a > C - c:
            dfs(a-C+c, b, C)
        else:
            dfs(0, b, a+c)

    if b != 0:
        if b > A - a:
            dfs(A, b-A+a, c)
        else:
            dfs(a+b, 0, c)
        if b > C - c:
            dfs(a, b-C+c, C)
        else:
            dfs(a, 0, b+c)

    if c != 0:
        if c > A - a:
            dfs(A, b, c-A+a)
        else:
            dfs(a+c, b, 0)
        if c > B - b:
            dfs(a, B, c-B+b)
        else:
            dfs(a, b+c, 0)


dfs(0, 0, C)
result = list(result)
result.sort()
for i in result:
    print(i, end=' ')
