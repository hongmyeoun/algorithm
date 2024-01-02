def solution(my_string):
    return ''.join([c.lower() if c.isupper() else c.upper() for c in my_string])

# swapcase() 대소문자를 바꿔줌
def solution(my_string):
    return my_string.swapcase()
