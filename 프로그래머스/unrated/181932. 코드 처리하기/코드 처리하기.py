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