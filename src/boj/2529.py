import sys

input = sys.stdin.readline

k = int(input())
sign = list(map(str, input().split()))
answer = []

def dfs(idx, current_num):
    if idx == k:
        answer.append(current_num)
        return

    last_num = int(current_num[-1])

    if sign[idx] == '>':
        for i in range(10):
            if not num[i] and last_num > i:
                num[i] = True
                dfs(idx+1, current_num + str(i))
                num[i] = False
    else:
        for i in range(10):
            if not num[i] and last_num < i:
                num[i] = True
                dfs(idx+1, current_num + str(i))
                num[i] = False

for i in range(10):
    num = [False] * 10
    num[i] = True
    dfs(0, str(i))

print(answer[-1])
print(answer[0])