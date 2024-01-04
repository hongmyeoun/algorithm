def solution(strArr):
    len_strArr = [len(i) for i in strArr]
    count_len = [len_strArr.count(i) for i in set(len_strArr)]
        
    return max(count_len)