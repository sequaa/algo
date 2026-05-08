from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    dic = defaultdict(int)
    for order in orders:
        order = sorted(order)
        for c in course:
            for menu in combinations(order, c):
                dic[menu] += 1
    for c in course:
        cnt = 2
        temp = []
        for key in dic.keys():
            if len(key) == c:
                if dic[key] > cnt:
                    temp = [''.join(key)]
                    cnt = dic[key]
                elif dic[key] == cnt:
                    temp.append(''.join(key))
        answer += temp
    return sorted(answer)