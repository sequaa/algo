import sys

input = sys.stdin.readline

n, m = map(int, input().split())

book_pos = list(map(int, input().split()))
max_len = max(max(book_pos), abs(min(book_pos)))

m_book = []
p_book = []

for book in book_pos:
    if book < 0:
        m_book.append(book)
    else:
        p_book.append(book)

m_book.sort(reverse=True)
p_book.sort()

m_list = []
while m_book:
    temp = []
    for i in range(m):
        try:
            temp.append(m_book.pop())
        except:
            continue
    m_list.append(temp)

p_list = []
while p_book:
    temp = []
    for i in range(m):
        try:
            temp.append(p_book.pop())
        except:
            continue
    p_list.append(temp)

cnt = 0
b_list = m_list + p_list

for b in b_list:
    if abs(b[0]) == max_len:
        cnt += abs(b[0])
    else:
        cnt += abs(b[0]) * 2
print(cnt)