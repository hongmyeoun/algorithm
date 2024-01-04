def solution(strArr):
    len_strArr = [len(i) for i in strArr]
    count_len = [len_strArr.count(i) for i in set(len_strArr)]
        
    return max(count_len)

처음에 count_len쪽에서 for i in len_strArr 로 접근했더니
대부분의 테스트 케이스에서 시간초과가 됐었다.
이전에 했던 set을 통해 for반복을 줄여서 해결
그래도 시간이 많이걸린다. 이건 input이 100000까지여서 그런거 같다.

# 이렇게 풀려고 생각했었던것
def solution(strArr):
    a=[0]*31
    for x in strArr: 
        a[len(x)]+=1
    return max(a)

