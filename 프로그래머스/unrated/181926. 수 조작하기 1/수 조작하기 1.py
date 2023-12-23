def solution(n, control):
    answer = n
    for i in control:
        if i == 'w':
            answer += 1
        elif i == 's':
            answer -= 1
        elif i == 'd':
            answer += 10
        elif i == 'a':
            answer -= 10
    return answer

# dictionary와 zip 생각을 왜못했지?
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10])) # zip([][]) => {'w': 1, 's': -1, 'd': 10, 'a': -10} 리스트를 튜프로 만들고, dict을 딕셔너리를 만듦
    return n + sum([key[c] for c in control]) # 더해지고 빼지는 값의 총합과 n을 더하는 로직
