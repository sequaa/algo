import sys

input = sys.stdin.readline

# t = int(input())
#
# for _ in range(t):
while True:
    try:
        x = int(input()) * 10**7
        n = int(input())
        lego = [int(input()) for _ in range(n)]

        lego.sort()
        start, end = 0, n-1

        check = False
        while start < end:
            if lego[start] + lego[end] == x:
                check = True
                print(' '.join(['yes', str(lego[start]), str(lego[end])]))
                break

            elif lego[start] + lego[end] > x:
                end -= 1

            else:
                start += 1

        if not check:
            print('danger')
    except:
        break