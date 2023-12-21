def solution(code):
    ret = ''
    mode = 0
    # code를 앞에서부터 읽으면서
    for idx, i in enumerate(code):
        # 만약 문자가 1이면
        if i == "1":
            # mode를 바꿉니다.(기본 mode == 0)
            mode = 1 if mode == 0 else 0
        else:
            # 여 부분은 줄이고 싶은데 못하겠음...
            if mode == 0:
                if idx % 2 == 0:
                    ret += i
            else:
                if idx % 2 == 1:
                    ret += i
    
    answer = 'EMPTY' if ret == '' else ret

    return answer

# 말도안되는 숏코딩
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"

# 또다른 방법 ^=
def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'
