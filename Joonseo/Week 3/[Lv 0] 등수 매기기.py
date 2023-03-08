def solution(score):
    answer = []
    li = []
    for i in score:
       li.append(sum(i)/2) # li에 각 인덱스의 평균값을 삽입
    sort_li = sorted(li, reverse = True) # sorted_li에 li를 내림차순 정렬하여 삽입
    for i in li: # i가 li의 값을 순회하면서
       answer.append(sort_li.index(i)+1) # sorted_li에 i가 있는 인덱스 + 1을 answer에 삽입
    return answer