def solution(p):
    if not p:
        return ""

    u, v = divide(p)

    if is_balanced(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'

        u = u[1:-1]
        temp = ""
        for c in u:
            if c == '(':
                temp += ')'
            else:
                temp += '('
        return answer + temp

def divide(w):
    cnt = 0
    for i in range(len(w)):
        if w[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return w[:i+1], w[i+1:]

def is_balanced(w):
    stack = []
    for c in w:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return True

