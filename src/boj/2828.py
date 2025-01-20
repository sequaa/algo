import sys

input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())

basket = [1, m]
cnt = 0
for _ in range(j):
    apple = int(input())
    if apple < basket[0]:
        temp = basket[0] - apple
        basket[0] -= temp
        basket[1] -= temp
        cnt += temp
    elif apple > basket[1]:
        temp = apple - basket[1]
        basket[0] += temp
        basket[1] += temp
        cnt += temp

print(cnt)