import sys

input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

while len(t) > len(s):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()
if t == s:
    print(1)
else:
    print(0)