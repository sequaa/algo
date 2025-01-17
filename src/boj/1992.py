import sys

input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().strip())) for _ in range(N)]


def qt(a, b, n):
    check = True
    for i in range(a, a+n):
        for j in range(b, b+n):
            if nums[a][b] != nums[i][j]:
                check = False
                break

    if check:
        return str(nums[a][b])
    else:
        return '(' + qt(a, b, n//2) + qt(a, b+n//2, n//2) + qt(a+n//2, b, n//2) + qt(a+n//2, b+n//2, n//2) + ')'


print(qt(0, 0, N))
