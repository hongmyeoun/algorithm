def solution(my_string, overwrite_string, s):
    if 1 <= len(overwrite_string) <= len(my_string) <= 1000:
        if 0 <= s <= len(my_string) - len(overwrite_string):
            # s전까지 + 덮어쓰기 + 덮어쓴 부분 이후(my_string) => 결국 덮어쓴게 아니긴한데,,, 모름
            # replace로는 첫번째 test 통과 못했음...
            # answer = my_string.replace(my_string[:s, s + len(overwrite_string):], overwrite_string)
            # TypeError: string indices must be integers

            answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
            
    return answer
