from collections import deque

def solution(begin, target, words):
    n = len(target)
    queue = deque([(begin, 0)])
    visited = set()
    while queue:
        current, cnt = queue.popleft()
        if current == target:
            return cnt
        for word in words:
            if word not in visited and is_available(current, word):
                visited.add(word)
                queue.append((word, cnt+1))

    return 0

def is_available(start, end):
    l = len(start)
    check = 0
    for i in range(l):
        if start[i] != end[i]:
            check += 1
        if check > 1:
            return False
    return True
