import sys

input = sys.stdin.readline
n = int(input())
nums = [input().strip() for _ in range(n)]

target = dict()
for num in nums:
    len_num = len(num)-1
    for i in num:
        if i in target:
            target[i] += 10**len_num
        else:
            target[i] = 10**len_num
        len_num -= 1

sorted_target = sorted(target.values(), reverse=True)
result = 0
cnt = 9
for t in sorted_target:
    result += t*cnt
    cnt -= 1

print(result)

