import sys

input = sys.stdin.readline

n = int(input())
m_nums = []
p_nums = []

for _ in range(n):
    num = int(input())
    if num > 0:
        p_nums.append(num)
    else:
        m_nums.append(num)

p_nums.sort()
m_nums.sort(reverse=True)
result = 0

while len(p_nums) >= 2 and p_nums[-1] > 1 and p_nums[-2] > 1:
    num1 = p_nums.pop()
    num2 = p_nums.pop()
    result += num1*num2

while len(m_nums) >= 2:
    num1 = m_nums.pop()
    num2 = m_nums.pop()
    result += num1*num2

result += sum(p_nums) + sum(m_nums)

print(result)
