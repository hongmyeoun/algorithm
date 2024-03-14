def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        
    return answer

충격과 공포의 내장함수
def Jaden_Case(s):
    return s.title()

하지만 이젠 안된다함(정답 1번에서 컷)

import string

s = "hello world"
formatted_string = string.capwords(s)
print(formatted_string)  # 출력: "Hello World"

string.capwords(s, sep) 함수는 string 모듈에 포함된 함수로서, 문자열 s를 받아서 단어의 첫 글자를 대문자로 변환하는 역할을 합니다. 두 번째 매개변수 sep은 단어를 구분하는 구분자(separator)를 지정합니다.

def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])
이건 맨 앞글자만 대문자가 되고 나머지가 소문자가 되지는 않는다.
