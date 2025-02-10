import sys

input = sys.stdin.readline


def check(s):
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        elif i == ']':
            if not stack:
                return False
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    if stack:
        return False
    else:
        return True


while True:
    input_str = input().rstrip()
    if input_str == '.':
        break

    if check(input_str):
        print('yes')
    else:
        print('no')
