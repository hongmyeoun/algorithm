def solution(array):
    set_array = list(set(array))
    num_count = [array.count(i) for i in set_array]
    answer = -1
    
    if num_count.count(max(num_count)) == 1:
        answer = set_array[num_count.index(max(num_count))]
        
    return answer

# 의사코드
    # count로 세면될듯?
    # 주사위랑 동일하게 맞춰놓고 최빈값이랑 최빈값 출현 횟수랑 다르면 -1 return
    # 실패
	# array = [1, 1, 1, 1, 2, 3, 3, 4]
	# num_count = [4, 4, 4, 4, 1, 2, 2, 1]
	# num_count.count(num_count) = [4, 4, 4, 4, 2, 2, 2, 2]
	# array = [1, 1, 1, 1, 2, 3, 3, 4, 3, 3]
	# num_count = [4, 4, 4, 4, 1, 4, 4, 1, 4, 4]
	# num_count.count(num_count) = [8, 8, 8, 8, 2 ,8, 8, 2, 8, 8]
	# max(num_count) != max([num_count.count(i) for i in num_count]) -> -1
	# 아니면 array[num_count.index(max(num_count))]
    
    # max([num_count.count(i) for i in num_count]) 1,1,1,1,1이 많아질때 문제가 생김
    # array를 set으로 받음
    # 그런후 array를 카운트
    # 최빈값을 세서 1개면 그값을 출력
    # 아니면 -1출력

