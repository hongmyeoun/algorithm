import re

def solution(numbers):
    english_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = list(range(0, 10))
    num_dict = dict(zip(english_num, num))
    
    pattern = '|'.join(num_dict.keys())
    matches = re.findall(pattern, numbers)
    answer = ''.join(str(num_dict[word]) for word in matches)
        
    return int(answer)