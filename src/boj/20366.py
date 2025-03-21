import sys


input = sys.stdin.readline

n = int(input())
snow = list(map(int, input().split()))

snow.sort()
min_diff = float('inf')

for i in range(n-3):
    for j in range(i+3, n):
        snowman1 = snow[i] + snow[j]
        start, end = i+1, j-1

        while start < end:
            snowman2 = snow[start] + snow[end]
            diff = abs(snowman1 - snowman2)
            min_diff = min(min_diff, diff)

            if snowman2 > snowman1:
                end -= 1
            else:
                start += 1

print(min_diff)
