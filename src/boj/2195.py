import sys
from collections import deque

input = sys.stdin.readline

s = list(input().rstrip())
p = list(input().rstrip())

copy = set()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        temp = ''.join(s[i:j])
        if temp not in copy:
            copy.add(temp)

queue = deque(p)
c = ''
cnt = 0
while queue:
    temp = queue.popleft()
    if c + temp not in copy:
        c = temp
        cnt += 1
    else:
        c += temp
print(cnt+1)