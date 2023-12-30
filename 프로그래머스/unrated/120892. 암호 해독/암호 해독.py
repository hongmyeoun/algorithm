def solution(cipher, code):
    # 4만큼 뛰어넘어가면서 슬라이싱
    return cipher[code-1::code]