def solution(name, yearning, photo):
    answer = []
    for i in photo:
        point = 0
        for n, y in zip(name, yearning):
            for man in i:
                if man == n:
                    point += y
        answer.append(point)
    return answer

# list를 순회하지 않고도 name[j]를 통해 값을 찾아 결과를 더할 수 있다. -> 이름이 중복이 안되니까...
def solution(name, yearning, photo):
    answer = []
    for i in photo:
        score=0
        for j in range(len(name)):
            if name[j] in i:
                score+=yearning[j]
        answer.append(score)
    return answer

# index로 풀이
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]

# dict로 풀이
def solution(name, yearning, photo):
    dictionary = dict(zip(name,yearning))
    scores = []
    for pt in photo:
        score = 0
        for p in pt:
            if p in dictionary:
                score += dictionary[p]
        scores.append(score)
    return scores

불필요한 반복문을 줄이는 방식으로 가야된다. 3중첩 반복문이어서 내껀 퍼포먼스가 좋지 않다.
-> 이름이 중복될 일이없는데 그걸 고려했음...
