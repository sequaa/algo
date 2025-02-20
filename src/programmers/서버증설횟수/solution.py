from collections import deque


def solution(players, m, k):
    answer = 0
    queue = deque()
    server_cnt = 0
    for i in range(24):
        while queue and queue[0][1]+k <= i:
            cnt, t = queue.popleft()
            server_cnt -= cnt
        if players[i] >= (server_cnt+1)*m:
            temp = players[i]//m - server_cnt
            server_cnt += temp
            answer += temp
            queue.append((temp, i))
    return answer
