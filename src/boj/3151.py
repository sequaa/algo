import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
num.sort()

cnt = 0
for i in range(n-2):
    if num[i] > 0:
        break

    start, end = i+1, n-1
    while start < end:
        temp = num[i] + num[start] + num[end]
        if temp == 0:
            if num[start] == num[end]:
                cnt += end - start
                start += 1
            else:
                j, k = start, end
                while num[j] == num[start] and j < end:
                    j += 1
                while num[k] == num[end] and k > start:
                    k -= 1
                cnt += (j-start)*(end-k)
                start, end = j, k
        elif temp < 0:
            start += 1
        else:
            end -= 1

print(cnt)