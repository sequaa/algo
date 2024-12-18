import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

start, end = 0, n-1

min_sum = 2000000000
pair = ()

while start < end:
    current_sum = num[start] + num[end]
    if abs(current_sum) < min_sum:
        min_sum = abs(current_sum)
        pair = (num[start], num[end])

    if current_sum < 0:
        start += 1
    else:
        end -= 1

print(pair[0], pair[1])
