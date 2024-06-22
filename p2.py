# 프로젝트 문제 2번
input = ")))()"


def problem2(input):
    F = 0
    B = 0
    
    for char in input:
        if char == '(':
            F += 1
        elif char == ')':
            if F > 0:
                F -= 1
            else:
                B += 1
    
    return F + B

result = problem2(input)

assert result == 3
print("정답입니다.")
