import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
s = input().strip()

cnt = defaultdict(int)
len_s = len(s)

result = 0
start = 0

for end in range(len_s):
    cnt[s[end]] += 1

    while len(cnt) > n:
        cnt[s[start]] -= 1
        if cnt[s[start]] == 0:
            del cnt[s[start]]
        start += 1

    result = max(result, end - start + 1)

print(result)