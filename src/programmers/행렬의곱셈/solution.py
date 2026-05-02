def solution(arr1, arr2):
    answer = []
    n = len(arr1)
    m = len(arr2)
    l = len(arr2[0])
    for i in range(n):
        result = []
        for j in range(l):
            temp = 0
            for k in range(m):
                temp += arr1[i][k] * arr2[k][j]
            result.append(temp)
        answer.append(result)
    return answer