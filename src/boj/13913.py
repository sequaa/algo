import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
# way_list = [n]
# visited[n] = True
# queue = deque([(0, way_list)])
#
# while queue:
#     cnt, way = queue.popleft()
#     current_node = way[-1]
#     if current_node == k:
#         print(cnt)
#         print(*way)
#         break
#
#     for i in (current_node-1, current_node+1, current_node*2):
#         if 0 <= i <= 100000 and not visited[i]:
#             next_way = way + [i]
#             queue.append((cnt+1, next_way))
#             visited[i] = True
# 기존 풀이 : 큐에 경로가 누적 되어 들어감. 코드가 직관적이나 next_way = way + [i]가 계속해서 새로운 리스트가 만들어 지는 형태라
# 시간 초과가 발생 -> 경로를 포함하는 bfs 문제에선 다른 풀이가 적용 되어야 함.

parent = {}
visited[n] = True
queue = deque([n])
parent[n] = -1

while queue:
    current_node = queue.popleft()
    if current_node == k:
        path = []
        cnt = -1
        while current_node != -1:
            path.append(current_node)
            current_node = parent[current_node]
            cnt += 1
        print(cnt)
        print(*path[::-1])
        break

    for next_node in (current_node-1, current_node+1, current_node*2):
        if 0 <= next_node <= 100000 and not visited[next_node]:
            visited[next_node] = True
            parent[next_node] = current_node
            queue.append(next_node)