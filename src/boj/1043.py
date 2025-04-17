import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trust = list(map(int, input().split()))
trust_cnt = trust[0]
trust_member = trust[1:]

party = []
parent = [i for i in range(n+1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root != y_root:
        parent[y_root] = x_root


for _ in range(m):
    data = list(map(int, input().split()))
    party_size = data[0]
    party_member = data[1:]
    party.append(party_member)

    for i in range(1, party_size):
        union(party_member[0], party_member[i])

trust_root = set(find(p) for p in trust_member)

result = 0
for i in party:
    if not any(find(p) in trust_root for p in i):
        result += 1

print(result)