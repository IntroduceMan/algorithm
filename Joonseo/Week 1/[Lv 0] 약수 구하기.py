def solution(n):
    answer = []
    for i in range(1,n+1): # n까지 반복하기
       if (n%i==0): # i가 n의 약수이면
          answer.append(i) # answer에 i를 추가하기
    return answer

n = int(input())
print(solution(n))