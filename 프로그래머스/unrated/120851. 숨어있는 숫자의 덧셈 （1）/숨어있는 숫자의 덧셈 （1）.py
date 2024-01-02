def solution(my_string):
    num = ['1','2','3','4','5','6','7','8','9']
    return sum(int(c) for c in my_string if c in num)

# isdisigt() 숫자인지 판별해주는거 같음
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
