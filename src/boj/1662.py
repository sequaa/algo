import sys

input = sys.stdin.readline

s = input().strip()


def decode(target):
    cnt = 0
    st = []
    temp = []
    multiple = 0

    check = False
    bracket_cnt = 0
    for i in target:
        if i == '(' and not check:
            multiple = int(temp.pop())
            check = True

        elif not check:
            temp.append(i)

        elif check:
            if i == '(':
                bracket_cnt += 1
                st.append(i)
            elif i == ')':
                if bracket_cnt > 0:
                    st.append(i)
                    bracket_cnt -= 1
                else:
                    cnt += multiple*decode(st)
                    st = []
                    check = False
            else:
                st.append(i)
    return len(temp) + cnt


print(decode(s))