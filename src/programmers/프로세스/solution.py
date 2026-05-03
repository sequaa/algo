from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    priorities.sort()
    time = 0

    while True:
        current_loc, current_prio = queue.popleft()
        if current_prio == priorities[-1]:
            priorities.pop()
            time += 1
            if current_loc == location:
                return time
        else:
            queue.append((current_loc, current_prio))