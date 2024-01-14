def solution(a, b):
    answer = ''
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if a-1 == 0:
        answer = week[(b - 1) % 7]
    else:
        days = 0
        for mon in range(1, a):
            days += month[mon]
        answer = week[(days + b - 1) % 7]
    return answer

# 1월 8일 계산
# a - 1 == 0
# 8 - 1 == 7
# 7 % 7 == 0 -> 금

# 1월 23일 계산
# a - 1 == 0
# 23 - 1 == 22
# 22 % 7 == 1 -> 토

# 2월 3일 계산
# a - 1 == 1 -> 31 + 3
# 34 - 1 == 33
# 33 % 7 == 5 -> 수 1월 30일 토, 31 일, 1 월, 2화, 3수

# 5월 24일 계산
# a - 1 == 4 -> 31 + 29 + 31 + 30 + 24
# 145 - 1 == 144
# 144 % 7 == 4 -> TUE

# datetime사용
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

# 인덱싱으로 날짜 값 계산
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]

딕셔너리 만드는 것보다 이렇게 인덱싱을 하는게 더 편할 것 같다.

# 번외 예술가
def getDayName(a,b):
    answer = ""
    if a>=2:
        b+=31
        if a>=3:
            b+=29#2월
            if a>=4:
                b+=31#3월
                if a>=5:
                    b+=30#4월
                    if a>=6:
                        b+=31#5월
                        if a>=7:
                            b+=30#6월
                            if a>=8:
                                b+=31#7월
                                if a>=9:
                                    b+=31#8월
                                    if a>=10:
                                        b+=30#9월
                                        if a>=11:
                                            b+=31#10월
                                            if a==12:
                                                b+=30#11월
    b=b%7

    if b==1:answer="FRI"
    elif b==2:answer="SAT" 
    elif b==3:answer="SUN"
    elif b==4:answer="MON"
    elif b==5:answer="TUE"
    elif b==6:answer="WED"
    else:answer="THU"
    return answer
