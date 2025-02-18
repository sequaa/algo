from itertools import combinations


def solution(n, q, ans):
    answer = 0
    m = len(q)
    comb = list(combinations(range(1, n+1), 5))
    for c in comb:
        check = True
        for i in range(m):
            cnt = 0
            for j in q[i]:
                if j in c:
                    cnt += 1
            if cnt != ans[i]:
                check = False
                break
        if check:
            answer += 1
    return answer
