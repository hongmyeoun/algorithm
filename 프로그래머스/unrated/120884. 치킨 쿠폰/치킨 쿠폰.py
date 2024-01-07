def solution(chicken):
    answer = 0
    while chicken >= 10:
        answer += chicken//10
        chicken = chicken//10 + chicken%10

    return answer

# 9로 나누는 식
def solution(chicken):
    return int(chicken*0.11111111111)

def solution(chicken):
    return (max(chicken,1)-1)//9

원래는 10마리마다 쿠폰이 생기니 10으로 나눠야 하지만, 서비스 치킨에 대한 쿠폰도 발생하므로 9로 나눔
하지만 실제로 9마리의 치킨으로는 서비스를 받지 못하기 때문에 -1을 넣어 9마리일 때 서비스가 생기지 않도록 수정
