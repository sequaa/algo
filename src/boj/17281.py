import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

innings = [list(map(int, input().split())) for _ in range(n)]

num_without_0 = [1, 2, 3, 4, 5, 6, 7, 8]
hit_num = list(permutations(num_without_0, 8))

cnt = 0
max_score = 0
for hit in hit_num:
    hit_list = list(hit)
    hit_list = hit_list[:3] + [0] + hit_list[3:]

    score = 0
    hitter = 0
    for inning in innings:
        out_count = 0
        runner = [0, 0, 0]
        while out_count < 3:
            current = inning[hit_list[hitter]]

            if current == 0:
                out_count += 1
            elif current == 1:
                score += runner[2]
                runner[2] = runner[1]
                runner[1] = runner[0]
                runner[0] = 1
            elif current == 2:
                score += runner[1] + runner[2]
                runner[2] = runner[0]
                runner[1] = 1
                runner[0] = 0
            elif current == 3:
                score += runner[0] + runner[1] + runner[2]
                runner = [0, 0, 1]
            else:
                score += runner[0] + runner[1] + runner[2] + 1
                runner = [0, 0, 0]

            hitter = (hitter + 1) % 9
    max_score = max(max_score, score)

print(max_score)
