def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    temp_one, temp_two, temp_three = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            temp_one += 1
        if answers[i] == two[i%len(two)]:
            temp_two += 1
        if answers[i] == three[i%len(three)]:
            temp_three += 1
    
    score = []
    score.append(temp_one)
    score.append(temp_two)
    score.append(temp_three)
    
    answer = []
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
            
    return answer
