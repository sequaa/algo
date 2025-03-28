import sys

input = sys.stdin.readline

N, R, C = map(int, input().split())


def find(n, r, c):
    if n == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        elif r == 1 and c == 1:
            return 3

    size = 2 ** (n-1)

    if r < size and c < size:
        return find(n-1, r, c)
    elif r < size and c >= size:
        return (size**2) + find(n-1, r, c-size)
    elif r >= size and c < size:
        return 2 * (size**2) + find(n-1, r-size, c)
    else:
        return 3 * (size**2) + find(n-1, r-size, c-size)


print(find(N, R, C))