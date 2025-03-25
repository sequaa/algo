import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

common = set(a) & set(b)

answer = []
while common:
    max1 = max(common)
    answer.append(max1)

    idx1 = a.index(max1)
    idx2 = b.index(max1)

    a = a[idx1+1:]
    b = b[idx2+1:]

    common = set(a) & set(b)

print(len(answer))
print(*answer)