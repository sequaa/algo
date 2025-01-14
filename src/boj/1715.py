import sys
import heapq

input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    heapq.heappush(nums, int(input()))

temp = 0
while nums:
    if len(nums) < 2:
        break

    num1 = heapq.heappop(nums)
    num2 = heapq.heappop(nums)
    temp += num1+num2
    heapq.heappush(nums, num1+num2)

print(temp)
