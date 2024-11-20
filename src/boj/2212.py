import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

sensor = list(map(int, input().split()))

sensor.sort()

diff = []

for i in range(1, n):
    diff.append(sensor[i] - sensor[i-1])

diff.sort()
print(sum(diff[:n-k]))
