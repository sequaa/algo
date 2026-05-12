def solution(k, ranges):
    ubak_seq = [k]
    answer = []
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3*k+1
        ubak_seq.append(k)

    n = len(ubak_seq) - 1

    for r in ranges:
        a = r[0]
        b = n + r[1]
        if a > b:
            answer.append(-1.0)
        elif a == b:
            answer.append(0.0)
        else:
            temp = 0.0
            for i in range(a,b):
                temp += (ubak_seq[i] + ubak_seq[i+1]) / 2.0
            answer.append(temp)

    return answer