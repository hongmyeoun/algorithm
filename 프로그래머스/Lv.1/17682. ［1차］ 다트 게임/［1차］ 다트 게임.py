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

# 정규식을 이용한 풀이
import re
def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0: # 첫번째에서 스타가 터졌을때 고려
            dart[i-1] *= 2 # 이전 값 두배
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]] # 기존 리스트를 사용

    answer = sum(dart)
    return answer

p = re.compile('(\d+)([SDT])([*#]?)')
문자를 세 부위로 나눔
(\d+) : \d는 숫자를 나타냄, +는 하나이상의 반복을 뜻함 -> 하나이상의 숫자가 반복되는 부분을 매칭해서 뽑아냄(끝날때)
([SDT]) : [SDT]는 'S', 'D', 'T'중 하나랑 매칭해서 뽑아냄
([*#]?) : '*', '#'중 하나가 있을수도 있고 없을 수도 있다. 있으면 그걸 뽑아냄, 없으면 빈값 ''을 줌

dart = p.findall(dartResult)
그렇게 뽑아낸 값들을 tuple묶고 list로 저장

ex) dartResult = "1S2D*3T" 
[('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]

# 문자열을 전체를 순회하면서 풀이
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k') # 10은 1,0으로 순회가 되기때문
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)

# 10을 안바꾸고 푼 풀이
def solution(dartResult):
    # 보너스 지수
    dart = {'S':1, 'D':2, 'T':3}
    # 점수를 저장할 리스트
    scores = []
    # 현재 순회 중인 문자의 인덱스
    n = 0

    for i, d in enumerate(dartResult):
        # 현재 문자가 'S', 'D', 'T' 중 하나인 경우
        if d in dart:
            # 해당 보너스 지수를 적용하여 점수를 리스트에 추가
            scores.append(int(dartResult[n:i])**dart[d])
        # 현재 문자가 '*'인 경우
        if d == "*":
            # 바로 전과 현재 점수를 2배로 만듦
            scores[-2:] = [x*2 for x in scores[-2:]]
        # 현재 문자가 '#'인 경우
        if d == "#":
            # 현재 점수를 -1배로 만듦
            scores[-1] = (-1)*scores[-1]
        # 숫자가 아닌 문자를 만난 경우, 다음 숫자의 시작 인덱스를 기록
        if not (d.isnumeric()):
            n = i+1

    # 최종 점수 계산
    return sum(scores)
