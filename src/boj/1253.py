import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()


def check(k):
    start, end = 0, n-1
    while start < end:

        if start == k:
            start += 1
        if end == k:
            end -= 1

        if start == end:
            continue

        if nums[start] + nums[end] > nums[k]:
            end -= 1
        elif nums[start] + nums[end] < nums[k]:
            start += 1
        else:
            return 1
    return 0


cnt = 0
for i in range(n):
    cnt += check(i)

print(cnt)
