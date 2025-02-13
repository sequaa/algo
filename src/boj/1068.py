import sys

input = sys.stdin.readline

n = int(input())

node = {}
for i in range(n):
    node[i] = []

parents = list(map(int, input().split()))
del_node = int(input())
for i in range(0, n):
    if parents[i] == -1:
        continue
    node[parents[i]].append(i)


def dfs(idx):
    while node[idx]:
        next_node = node[idx].pop()
        dfs(next_node)

    del node[idx]


dfs(del_node)
cnt = 0
for i in node.keys():
    if not node[i]:
        cnt += 1
    if node[i] == [del_node]:
        cnt += 1
print(cnt)
