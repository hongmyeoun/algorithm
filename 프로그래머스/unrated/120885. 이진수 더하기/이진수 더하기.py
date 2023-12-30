def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2)).replace("0b","")

bin1과 bin2를 십진수로 바꾼뒤 계산
answer를 다시 이진수로 변환

이 과정에서 bin()을 사용하게 되면, 값이 str값으로 생성 되지만, "0b101"과 같이 binary라는 걸 명시해주게 된다.
이 "0b"를 없에기 위해 .replace("0b","")를 사용하거나, [2:]를 사용 할 수 있는데
각각의 장단점이 있다.
[2:] 를 사용하면, 코드가 간결해지고 가독성이 좋아지는 장점이 있다. 다만, 새로운 문자열을 생성하는 것이기 때문에 매우 큰 값이라면 성능문제가 생길 수 있다.
.replace("0b","") 를 사용하면 문자열을 생성하지 않고 기존의 문자열을 수정하기 때문에 메모리효율적일 수 있다. 단, 코드가 약간 길어진다.

# 다른 사람의 풀이
def solution(bin1, bin2):
    answer = 0
    bin1_size = len(bin1)
    bin2_size = len(bin2)

    sum = 0

    for i in bin1:
        sum += int(i) * (2 ** (bin1_size - 1))
        bin1_size -= 1

    for i in bin2:
        sum += int(i) * (2 ** (bin2_size - 1))
        bin2_size -= 1

    answer = str(bin(sum))[2:]

    return answer

이 식은 받은 값을 10진수로 바꾸고, 계산한뒤 다시 2진수로 바꾸는데,
10진수로 바꾸는 과정은 함수를 사용하지 않고 만들었지만, 결국 2진수로 바꿀때 bin()함수를 사용한다.
그러면 int(x,2)를 왜 안쓴거지...?
