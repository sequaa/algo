def solution(skill, skill_trees):
    answer = 0
    available_tree = set()
    available_tree.add('')
    temp = ''
    for i in skill:
        temp += i
        available_tree.add(temp)

    for tree in skill_trees:
        temp = ''
        for c in tree:
            if c in skill:
                temp += c
        if temp in available_tree:
            answer += 1
    return answer
