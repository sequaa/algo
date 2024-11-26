import sys

input = sys.stdin.readline

s = input().rstrip()

bomb = input().rstrip()

stack = []
bomb_len = len(bomb)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
