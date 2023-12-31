def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    return ''.join([morse[word] for word in letter.split(' ')])

# 의사코드
    영어가 싫어요와 동일할 듯?
    replace로 바꿔줬던거 같은데
        
        for key in morse.keys():
            if key in letter:
                letter = letter.replace(key, morse[key])
        이렇게 하니 "eeee e aee aee mt" 결과가 나옴
    
    이 아니라, 공백으로 단어를 나누고 morse에서 value를 찾아 가져오기

# 리스트 컴프리헨션과 제너레이터
squared_list = [x**2 for x in range(1, 6)] # 출력: [1, 4, 9, 16, 25]
squared_generator = (x**2 for x in range(1, 6)) # 출력: <generator object <genexpr> at 0x...>

메모리
- 리스트 컴프리헨션
전체 리스트를 한 번에 메모리에 생성, 데이터 셋이 커지면 부담

- 제너레이터
필요한 값만 생성, 필요한 시점에 값을 생성, 메모리 효율적

사용 시점
- 리스트 컴프리헨션
리스트로 바로 사용 가능, 한번에 모든값 계산 후 저장할때 유용

- 제너레이터
필요할 때마다 값을 생성 할 때 유용

따라서 이 문제에 메모리를 고려한다면, 제너레이터를, 추후 재활용이 필요하다면 리스트컴프리헨션을 사용
