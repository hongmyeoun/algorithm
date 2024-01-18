def solution(lottos, win_nums):
    check = 0
    for num in win_nums:
        if num in lottos:
            check += 1
        
        if check == 6:
            return [1, 1]
    
    lotto_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    maximum = lotto_dict[lottos.count(0)+check]
    minimum = lotto_dict[check]
    return [maximum, minimum]

# win_nums와 lottos가 몇개 일치하는지 확인
# 같은 수 check -> 몇 개인지
# 만약 check가 6이면 최고 당첨, 최저 당첨 1
# 0의 개수를 셈
# 최고 당첨 순위 -> check + 0의 개수
# 최저 당첨 순위 -> check의 개수