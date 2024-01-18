def solution(X, Y):
    answer = []
    dict_Y = {}
    for idx, num in enumerate(Y):
        if num not in dict_Y: # dict_Y에 key값이 없다면
            dict_Y[num] = [idx]
        else:
            dict_Y[num].append(idx)
            
    for i in X:
        if i in dict_Y and dict_Y[i]:
            answer.append(i)
            dict_Y[i].pop()
            
    answer.sort(reverse=True)
    
    if not answer:
        return '-1'
    elif answer[0] == '0':
        return '0'
        
    return ''.join(answer)

# X를 순회하면서 Y와 같은 값이면 result에 추가
# 같은 값이 나오면 Y에서 그 값을 하나 뺌
# 만약 result가 없다면 -1을 추가해서 반환

dictionary로 조회를 하면 시간복잡도가 O(1)까지 줄어든다


# def solution(X, Y):
#     answer = ''
#     X = ''.join(sorted(X, reverse=True))
#     Y = ''.join(sorted(Y, reverse=True))
#     for i in X:
#         if i in Y:
#             answer += i
#             Y = Y[:Y.index(i)] + Y[Y.index(i)+1:]
    
#     if not answer:
#         return '-1'
#     elif answer[0] == '0':
#         answer = '0'
        
#     return answer

# def solution(X, Y):
#     answer = []
#     Y = list(Y)
#     for i in X:
#         if i in Y:
#             answer.append(i)
#             Y[Y.index(i)] = None
            
#     answer.sort(reverse=True)
    
#     if not answer:
#         return '-1'
#     elif answer[0] == '0':
#         return '0'
        
#     return ''.join(answer)

# 시간초과

# counter 풀이
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer

collection 카운터 쓰세요. 그게 10배 빠릅니다. 카운트 실행할때마다 O(n) 이에요 (n=len(str))

