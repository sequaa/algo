import sys

input = sys.stdin.readline

n = int(input())

s = [input().rstrip() for _ in range(n)]

result = ""

start, end = 0, n-1

while start <= end:
    if s[start] < s[end]:
        result += s[start]
        start += 1
    elif s[start] > s[end]:
        result += s[end]
        end -= 1
    else:
        if start == end:
            result += s[start]
            break
        next_idx = 1
        ns = start + next_idx
        ne = end - next_idx
        while ns <= ne:
            if s[ns] < s[ne]:
                result += s[start]
                start += 1
                break
            elif s[ns] > s[ne]:
                result += s[end]
                end -= 1
                break
            else:
                next_idx += 1

cnt = 0
for i in result:
    cnt += 1
    print(i, end='')
    if cnt == 80:
        print('\n')
        cnt = 1