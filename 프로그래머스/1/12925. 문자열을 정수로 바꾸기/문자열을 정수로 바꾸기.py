def solution(s):
    return int(s)

# 어려운 풀이
def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result

한자리 수씩 더해서 리턴하는 것
