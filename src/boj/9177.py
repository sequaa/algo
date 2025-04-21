import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


def check(str1, str2, str3):
    len1, len2 = len(str1), len(str2)
    queue = deque()
    visited = set()

    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()
        z = x + y

        if z == len(str3):
            return 'yes'

        if x < len1 and str1[x] == str3[z] and (x+1, y) not in visited:
            visited.add((x+1, y))
            queue.append((x+1, y))

        if y < len2 and str2[y] == str3[z] and (x, y+1) not in visited:
            visited.add((x, y+1))
            queue.append((x, y+1))

    return 'no'


for i in range(1, n+1):
    a, b, c = map(str, input().split())
    print("Data set {}: {}".format(i, check(a, b, c)))