def solution(bin1, bin2):
    # 방법 1
    # bin1과 bin2를 십진수로 바꾼뒤 계산
    # answer를 다시 이진수로 변환
    return bin(int(bin1, 2) + int(bin2, 2)).replace("0b","")