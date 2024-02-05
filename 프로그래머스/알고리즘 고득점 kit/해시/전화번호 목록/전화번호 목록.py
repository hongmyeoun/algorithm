# 하지만 해시를 이용한 풀이는 아님
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True
    
오름차순으로 정렬을 한뒤
순회하면서 현재값과 다음값의 접두어 비교
만약 같으면 False 반환

# 해시를 이용한 풀이
def solution(phone_book):
    phone_set = set(phone_book)

    for number in phone_book:
        current_prefix = ""
        for digit in number:
            current_prefix += digit
            if current_prefix in phone_set and current_prefix != number:
                return False

    return True

하지만 시간은 비슷함

# 이 풀이는 효율성 테스트 통과 못함
def solution(phone_book):
    answer = True
    phone_dic = dict()
    for i in phone_book:
        phone_dic[i] = len(i) - 1
    
    for c_key, c_value in phone_dic.items():
        for n_key, n_value in phone_dic.items():
            
            if c_value > n_value or c_key == n_key:
                continue
            if c_key == n_key[:c_value+1]:
                answer = False
                return answer
    
    return answer

value값을 비교해서 더 작은 쪽이 큰쪽에 앞부분과 같은지 확인
이 확인하는 과정은 작은쪽의 value만큼 큰쪽에서 확인 ex) 작은쪽key == 큰쪽[:작은쪽 value+1]
이런 경우가 있다면 answer가 false를 리턴하면서 종료
