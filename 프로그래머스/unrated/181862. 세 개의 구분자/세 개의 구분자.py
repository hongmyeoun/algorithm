def solution(myStr):
    split_word = ['a','b','c']
    for i in split_word:
        myStr = myStr.replace(i, '1')

    answer = [c for c in myStr.split('1') if c != '']

    return answer if answer else ['EMPTY']