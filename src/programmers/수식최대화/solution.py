from itertools import permutations

def solution(expression):
    answer = 0
    for operators in permutations(['+','-','*'],3):
        temp1 = []
        for ex1 in expression.split(operators[0]):
            temp2 = []
            for ex2 in ex1.split(operators[1]):
                temp3 = []
                for ex3 in ex2.split(operators[2]):
                    temp3.append(ex3)
                temp2.append(calculate(temp3, operators[2]))
            temp1.append(calculate(temp2, operators[1]))
        answer = max(answer, abs(calculate(temp1, operators[0])))
    return answer

def calculate(nums, operator):
    output = int(nums[0])
    for idx, num in enumerate(nums):
        if idx > 0:
            if operator == '+':
                output += int(num)
            elif operator == '-':
                output -= int(num)
            elif operator == '*':
                output *= int(num)
    return output
