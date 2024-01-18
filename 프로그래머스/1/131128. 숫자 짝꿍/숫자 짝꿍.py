def solution(X, Y):
    answer = []
    dict_Y = {}
    for idx, num in enumerate(Y):
        if num not in dict_Y:
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