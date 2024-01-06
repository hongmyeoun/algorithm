def solution(myStr):
    split_word = ['a','b','c']
    for i in split_word:
        myStr = myStr.replace(i, '1')

    answer = [c for c in myStr.split('1') if c != '']

    return answer if answer else ['EMPTY']

# split으로 공백없애기
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']
