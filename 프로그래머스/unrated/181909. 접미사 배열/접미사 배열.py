solution = lambda my_string: sorted([my_string[-i:] for i in range(len(my_string))])

# 첫 풀이는 이러함

def solution(my_string):
    answer = [my_string[-i:] for i in range(len(my_string))]
    return answer.sort()

이렇게 하니 return 값이 None이 나옴.
이는 list.sort()는 반환할 값이 없기 때문이다. sort()는 원본 list를 정렬해주는 함수이기 때문에 반환하는게 없다.
따라서

def solution(my_string):
    answer = [my_string[-i:] for i in range(len(my_string))]
    answer.sort()
    return answer

이렇게 써줘야 정렬이 된다.

# sorted()
  
def solution(my_string):
    return sorted([my_string[-i:] for i in range(len(my_string))])

그에 비해 sorted()는 정렬한 list를 반환하는 함수이므로 정렬된 새 list를 반환하기 때문에 이렇게 사용이 가능하다.

sort()와 sorted()의 차이

sort()
my_list = [1,3,2,5]
result = my_list.sort()
print(result) # None
print(my_list) # [1,2,3,5]

sorted()
my_list = [1,3,2,5]
result = sorted(my_list)
print(result) # [1,2,3,5]
print(my_list) = [1,3,2,5]
