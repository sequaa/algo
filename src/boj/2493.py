import sys

input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))

result = []
stack = []
for i in range(n):
    while stack and tower[stack[-1]] < tower[i]:
        stack.pop()
    if stack:
        result.append(stack[-1]+1)
    else:
        result.append(0)
    stack.append(i)

print(*result)
