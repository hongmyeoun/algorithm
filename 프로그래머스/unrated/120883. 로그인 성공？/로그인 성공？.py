# 가독성 좋게(?), 읽기 쉽게만 만들어놓은 제출한 코드, enumerate()를 사용 안해도 됐었을듯...
def solution(id_pw, db):
    answer = ''
    input_id = id_pw[0]
    input_pw = id_pw[1]
    for idx, db_id_pw in enumerate(db):
        user_id, user_pw = db_id_pw
        if input_id == user_id and input_pw == user_pw:
            answer = 'login'
            break
        if input_id == user_id and input_pw != user_pw:
            answer = 'wrong pw'
            break
        if input_id != user_id:
            answer = 'fail'
    return answer

test 1을 통과 하지 못했는데, list를 순회하고 마지막 요소에 대해서 answer를 출력하는 것 같아, login과 wrong pw일때는 순회를 종료시킴

# :=, dict, get을 사용한 풀이
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

파이썬 3.8 이상부터 사용할 수 있는 (:=) 월러스 연산자를 이용한 풀이
db를 dict으로 만들어 id를 key, pw를 value로 만듦
.get(id_pw[0])로 입력한 id를 db에서 찾아 그 value(pw)를 가져옴
즉 db에서 id가 같을때 그 id에 대한 db에 pw를 가져오는것
가져온 값을 db_pw에 저장하고 반환, 이때 db_pw에 None값이 들어오면, 조건문이 False가 되면서 'fail'을 반환
db_pw가 있을때, 입력한 pw와 db_pw를 비교
