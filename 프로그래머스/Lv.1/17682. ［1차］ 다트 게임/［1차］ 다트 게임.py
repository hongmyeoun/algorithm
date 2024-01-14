def solution(dartResult):
    
    sdr = split_input(dartResult)
    SDT = {'S':1,'D':2,'T':3}
    
    answer = 0
    st = 0
    nd = 0
    rd = 0
    
    for idx, i in enumerate(sdr):
        if i[-1] == '':
            if idx == 0:
                st = int(i[0])**SDT[i[1]]
            elif idx == 1:
                nd = int(i[0])**SDT[i[1]]
            else:
                rd = int(i[0])**SDT[i[1]]
        elif i[-1] == '*':
            if idx == 0:
                st = (int(i[0])**SDT[i[1]])*2
            elif idx == 1:
                st *= 2
                nd = (int(i[0])**SDT[i[1]])*2
            else:
                nd *= 2
                rd = (int(i[0])**SDT[i[1]])*2
        elif i[-1] == '#':
            if idx == 0:
                st = (int(i[0])**SDT[i[1]])*(-1)
            if idx == 1:
                nd = (int(i[0])**SDT[i[1]])*(-1)
            if idx == 2:
                rd = (int(i[0])**SDT[i[1]])*(-1)
    answer = st + nd + rd
    return answer

def split_input(input_str):
    result = []
    current_item = ""
    
    for char in input_str:
        if char.isdigit():
            current_item += char
        else:
            if current_item:
                result.append([current_item])
                current_item = ""
            result[-1].append(char)

    # 모든 문자열의 길이를 3으로 맞추기
    max_length = 3
    for sublist in result:
        sublist.extend([''] * (max_length - len(sublist)))

    return result


# * : 스타상, 해당점수와 바로전 점수를 두배로 만듦, 만역 처음에 뜨면 그 점수만 2배, 중첩가능 4배가됨
# # : 아차상, 해당점수를 -로, 스타상과 중첩됨 -로 중첩가능
# S, D, T는 점수마다 하나씩 존재

# 점수|보너스|[옵션]
# 1S2D*3T = 1점Single, 2점Double*, 3점Triple
# (1 + 2**2)*2 + 3**3
# 1D2S#10S = 1점Double, 2점Sigle#, 10점Single
# 1**2 + 2**1*(-1) + 10**1
# 1S*2T*3S = 1점Single*, 2점Triple*, 3점Single
# ((1**1)*2 + 2**3)*2 + 3**1

# 숫자로 split가능?
# dartResult를 돌면서 그 값이 숫자면 현재 값으로 추가
# 그 값이 숫자가 아니면
# 현재 값인 숫자를 score에 append하고 초기화
# score에 마지막 요소에 현재 순회중인 값을 넣어줌
