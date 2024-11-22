T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input().strip())) for _ in range(n)]

    result = 0
    for i in range(n//2):
        for j in range(n//2-i, n//2+i+1):
            result += graph[i][j]
    cnt = n//2
    for i in range(n//2, n):
        for j in range(n//2-cnt, n//2+cnt+1):
            result += graph[i][j]
        cnt -= 1
    print(result)