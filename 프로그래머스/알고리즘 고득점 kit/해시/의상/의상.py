def solution(clothes):
    answer = 1
    c_dic = {}
    for c in clothes:
        c_type = c[1]

        if c_type in c_dic:
            c_dic[c_type] += 1
        else:
            c_dic[c_type] = 1
            
    for c in c_dic.values():
        answer *= (c+1)
            
    return answer - 1

# clothes 리스트를 순회하면서 dict에 넣음
# dict_key에는 의상의 종류가 들어감
# dict_value에는 의상의 개수가 들어감
# 결과에 dict_value + 1 값을 곱함 -> 옷을 입지 않는 경우의수 하나 추가
# 최종 결과에서 옷을 아예 입지 않는 경우 1가지를 제거
