def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in range(len(babbling)):
        for j in baby:
            babbling[i] = babbling[i].replace(j,'1')
        if all(c=='1' for c in babbling[i]):
            answer += 1
            
    return answer
# babbling의 단어에서 baby에 포함된 단어를 1로 replace 시도했을때
# 1이면 count

# 맨처음ㅇ 풀려던 방법
def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c

replace까지는 했는데, 그이후 처리를 하지 못해서 풀지 못하고 있었음
이런식으로 일회용으로 사용하면서 바로 count를 하는 방식으로 생각해볼것

# re 를 사용(정규식)
import re
def solution(babbling):
    answer = 0
    for char in babbling:
        if re.match(r"^(aya|ye|woo|ma)+$", char):
            answer += 1
    return answer

정규식

정규식(Regular Expression 또는 regex)은 문자열의 패턴을 표현하는 데 사용되는 형식 언어입니다. 
이는 주로 특정한 문자열 패턴을 찾거나, 대체하거나, 추출하는 등의 문자열 작업에 활용됩니다.
정규식은 강력하면서도 유연한 문자열 처리 도구로 자주 사용됩니다.

정규식은 다양한 메타문자(meta-characters)와 문자들로 구성됩니다. 
몇 가지 주요 메타문자의 예는 다음과 같습니다:

. (마침표): 어떤 한 문자와 일치합니다.
^ (캐럿): 문자열의 시작 부분과 일치합니다.
$ (달러 기호): 문자열의 끝 부분과 일치합니다.
*: 앞에 오는 문자가 0회 이상 반복될 때 일치합니다.
+: 앞에 오는 문자가 1회 이상 반복될 때 일치합니다.
?: 앞에 오는 문자가 0회 또는 1회 반복될 때 일치합니다.
[]: 괄호 안의 어떤 문자든지 일치합니다.
| (파이프): "또는"을 나타내어 주어진 두 패턴 중 하나와 일치합니다.

예를 들어, 정규식 ^abc는 문자열이 "abc"로 시작하는지를 확인하고, a.b는 "a" 다음에 아무 문자 하나가 오고, 그 다음에 "b"가 오는 패턴과 일치합니다.
