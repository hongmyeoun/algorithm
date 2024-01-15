def solution(s):
    answer = []
    check = []
    for c in range(len(s)):
        if s[c] not in check:
            answer.append(-1)
            check.append(s[c])
        else:
            answer.append(c-(len(check) - check[::-1].index(s[c]) - 1))
            check.append(s[c])
    return answer

# 그 글자가 언제 어디서 나왔는지 저장을 해야함
# 저장된게 없다면 -1, 있다면 그 위치와 현재 위치를 빼줌
# 어떻게함?
# 일단 check 리스트를 만들어서 값을 저장
# 저장하기 전에 값이 있는지 확인을하고 추가해줌
# 값이 없다면 -1을 답에 추가해주고, check에 값을 추가
# check에 중복요소가 있다면
# check에 뒤에서부터 중복요소의 index를 가져와 현재 index에서 뺀값을 답에 추가
# check에 현재값을 추가

# dict이용
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer

내 풀이의 check를 dic으로 만들어 풀이

두 풀이의 시간복잡도

첫 번째 해결책에서는 리스트 check을 사용하여 지금까지 만난 문자를 추적합니다. 
각 문자의 마지막 발생 위치는 [::-1].index(s[c])를 사용하여 찾으며, 거리는 그에 따라 계산됩니다.
이 해결책은 각 문자마다 check 리스트에서 마지막 발생을 검색하므로 시간 복잡도가 O(n^2)입니다. 
왜냐하면 각 문자에 대해 O(n) 시간이 걸리기 때문입니다.

반면에 두 번째 해결책은 각 문자의 최근 인덱스를 문자열에서 저장하기 위해 사전 dic을 사용합니다. 
사전을 사용하는 주된 이점은 각 문자의 마지막 인덱스에 상수 시간(O(1))으로 액세스할 수 있다는 것입니다. 
따라서 두 번째 해결책의 전체 시간 복잡도는 O(n)이 되며, 이는 첫 번째 해결책보다 효율적입니다.    
