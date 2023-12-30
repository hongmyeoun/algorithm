def solution(cipher, code):
    # 4만큼 뛰어넘어가면서 슬라이싱
    return cipher[code-1::code]

# range로 슬라이싱
def solution(cipher, code):
    return ''.join(cipher[i] for i in range(code-1,len(cipher),code))
