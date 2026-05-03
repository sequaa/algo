def solution(brown, yellow):
    answer = []
    n = 3
    while True:
        for m in range(1, n+1):
            if (n * m) >= (brown + yellow):
                if (n * m) == (brown + yellow):
                    if (n-2) * (m-2) == yellow:
                        answer.append(n)
                        answer.append(m)
                        return answer
                break
        n += 1


# 리턴에 n,m이 들어가면 n*m = brown + yellow
# n >= m 이니까 n을 1부터 늘리면서 m을 n 까지 늘리면서 n * m 이 brown + yellow 되면 출력
