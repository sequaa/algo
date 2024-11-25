import sys

input = sys.stdin.readline

t = int(input())


def check():
    for i in range(len(num_list)-1):
        len_front = len(num_list[i])
        len_back = len(num_list[i+1])
        if len_front < len_back and num_list[i] == num_list[i+1][:len_front]:
            print("NO")
            return
    print("YES")


for _ in range(t):
    n = int(input())

    num_list = []
    for _ in range(n):
        num_list.append(str(input().rstrip()))

    num_list.sort()
    check()
