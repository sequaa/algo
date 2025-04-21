import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

inc = [1] * n
dec = [1] * n
for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            inc[i] = max(inc[i], inc[j]+1)

num.reverse()
for i in range(n):
    for k in range(i):
        if num[i] > num[k]:
            dec[i] = max(dec[i], dec[k]+1)

dec.reverse()

result = 0
for i in range(n):
    result = max(result, inc[i]+dec[i])
print(result-1)