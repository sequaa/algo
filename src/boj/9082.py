import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().strip()))
    mine = list(input().strip())

    cnt = 0
    for i in range(n):
        if i == 0:
            if nums[i] != 0 and nums[i+1] != 0:
                nums[i] -= 1
                nums[i+1] -= 1
                cnt += 1
        elif i == n-1:
            if nums[i-1] != 0 and nums[i] != 0:
                nums[i-1] -= 1
                nums[i] -= 1
                cnt += 1
        else:
            if nums[i-1] != 0 and nums[i] != 0 and nums[i+1] != 0:
                nums[i-1] -= 1
                nums[i] -= 1
                nums[i+1] -= 1
                cnt += 1
    print(cnt)