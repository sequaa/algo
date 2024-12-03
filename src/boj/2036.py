import sys

input = sys.stdin.readline

n = int(input())

m_num = []
p_num = []

for _ in range(n):
    num = int(input())
    if num > 0:
        p_num.append(num)
    else:
        m_num.append(num)

m_num.sort(reverse=True)
p_num.sort()

score = 0

while p_num:
    if len(p_num) >= 2:
        temp1 = p_num.pop()
        temp2 = p_num.pop()
        score += max(temp1*temp2, temp1+temp2)
    else:
        score += p_num.pop()

while m_num:
    if len(m_num) > 1:
        temp1 = m_num.pop()
        temp2 = m_num.pop()
        score += temp1 * temp2
    else:
        score += m_num.pop()

print(score)