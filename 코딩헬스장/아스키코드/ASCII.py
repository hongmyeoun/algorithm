# 문자를 입력받으면 아스키코드 10진수 int로 전환하는 함수
def AtoI(count = 0):
    if count < 1:
        ascii = input("문자 한 글자를 써주세요 : ")

    while len(ascii) != 1:
        count += 1
        ascii = input(f"{len(ascii)}자리 글자입니다...문자 한 글자만 써주세요({count}) : ")

    print(f"'{ascii}' -> {ord(ascii)}")

AtoI()
# 결과
# 문자 한 글자를 써주세요 : A
# 'A' -> 65

# 문자 한 글자를 써주세요 : 4
# '4' -> 52

# 문자 한 글자를 써주세요 : 22
# 2자리 글자입니다...문자 한 글자만 써주세요(1) : 333
# 3자리 글자입니다...문자 한 글자만 써주세요(2) : 44444
# 5자리 글자입니다...문자 한 글자만 써주세요(3) : a
# 'a' -> 97

# 0~127 사이의 int 값을 입력받으면 아스키코드에 해당하는 문자로 전환하는 함수
def ItoA(count = 0):

    try:
        if count < 1:
            number = int(input("0~127의 정수값을 입력해주세요 : "))
        else:
            number = int(input(f"0~127의 정수값을 입력해주세요({count}) : "))
        while number < 0 or number >= 128:
            count += 1
            number = int(input(f"0~127의 정수값을 입력해주세요({count}) : "))

        print(f"{number} -> '{chr(number)}'")

    except ValueError:
        print("실수값 입니다.", end=" ")
        count += 1
        return ItoA(count)

ItoA()
# 결과 
# 0~127의 정수값을 입력해주세요 : 97
# 97 -> 'a'

# 0~127의 정수값을 입력해주세요 : 48
# 48 -> '0'

# 0~127의 정수값을 입력해주세요 : -1
# 0~127의 정수값을 입력해주세요(2) : 0.3
# 실수값 입니다. 0~127의 정수값을 입력해주세요(3) : 128
# 0~127의 정수값을 입력해주세요(4) : 65
# 65 -> 'A'

# 문자를 입력받으면 아스키코드 10진수 int로 전환하고
# 0~127 사이의 int 값을 입력받으면 아스키코드에 해당하는 문자로 전환하는 함수
def ASCII_CODE():
    answer = input("아스키코드를 10진수로 바꾸려면 atoi, 10진수를 아스키코드로 바꾸려면 itoa를 써주세요 : ")
    count = 0
    while answer != "atoi" and answer != "itoa":
        count += 1
        answer = input(f"atoi(ASCII->int) 또는 itoa(int->ASCII)를 입력해주세요({count}) : ")

    if answer == "atoi":
        AtoI()
    elif answer == "itoa":
        ItoA()

ASCII_CODE()
# 결과
# 아스키코드를 10진수로 바꾸려면 atoi, 10진수를 아스키코드로 바꾸려면 itoa를 써주세요 : d
# atoi(ASCII->int) 또는 itoa(int->ASCII)를 입력해주세요(1) : j
# atoi(ASCII->int) 또는 itoa(int->ASCII)를 입력해주세요(2) : k
# atoi(ASCII->int) 또는 itoa(int->ASCII)를 입력해주세요(3) : atoiitoa
# atoi(ASCII->int) 또는 itoa(int->ASCII)를 입력해주세요(4) : atoij
# atoi(ASCII->int) 또는 itoa(int->ASCII)를 입력해주세요(5) : aoti
# atoi(ASCII->int) 또는 itoa(int->ASCII)를 입력해주세요(6) : atoi
# 문자 한 글자를 써주세요 : k
# 'k' -> 107

# 아스키코드를 10진수로 바꾸려면 atoi, 10진수를 아스키코드로 바꾸려면 itoa를 써주세요 : iota
# 0~127의 정수값을 입력해주세요 : 68
# 68 -> 'D'