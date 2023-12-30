# re 라이브러리를 사용한 풀이
import re

def solution(numbers):
    english_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = list(range(0, 10))
    num_dict = dict(zip(english_num, num))
    
    pattern = '|'.join(num_dict.keys())
    matches = re.findall(pattern, numbers)
    answer = ''.join(str(num_dict[word]) for word in matches)
        
    return int(answer)

# 라이브러리를 사용하지 않은 풀이
def solution(numbers):
    english_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = list(range(0, 10))
    num_dict = dict(zip(english_num, num))
    
    for number in num_dict.keys():
        numbers = numbers.replace(number, str(num_dict[number]))
        
    return int(numbers)

# dict를 만들지 않고 푼 풀이
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

str.replace()를 사용할 때 처음에 리스트를 그냥 넣으려 했으나 못넣어서 방법을 달리했더니 풀렸다.
