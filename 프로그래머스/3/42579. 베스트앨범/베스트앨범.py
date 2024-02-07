def solution(genres, plays):
    answer = []
    song_dict = {}
    
    for idx, genre in enumerate(genres):
        if genre not in song_dict:
            song_dict[genre] = []
        song_dict[genre].append((idx, plays[idx]))

    genre_play_sum = [(genre, sum(play for _, play in songs)) for genre, songs in song_dict.items()]
    genre_play_sum.sort(key=lambda x: x[1], reverse=True)

    for genre, _ in genre_play_sum:
        songs = song_dict[genre]
        songs.sort(key=lambda x: (-x[1], x[0]))
        for i in range(min(2, len(songs))):
            answer.append(songs[i][0])

    return answer

의사코드
    dict에 장르를 key, 인덱스와 재생수인 plays는 value값으로 저장
    만약 장르가 없으면 []로 생성
    (idx, plays[idx])를 append
    장르별 플레이 횟수의 합을 구함
    장르별 플레이 횟수를 내림차순으로 정렬
    장르별 플레이 횟수의 장르를 순회
    dict에 value값을 내림차순으로 정렬
    정렬된 value값중 최대 두개까지 answer에 append

# dict을 두개 사용한 풀이
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)): # zip()도 enumerate()안에 들어가는걸 깨달음!
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

dic1은 인덱스외 플레이횟수
dic2는 플레이 총합
이 둘을 정렬해서 값을 추가

