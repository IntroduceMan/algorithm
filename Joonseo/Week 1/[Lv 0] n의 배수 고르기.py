def solution(n, numlist):
    answer = []
    for i in numlist: # numlist를 순회하며 반복한다
       if(i%n==0): # 만약 numlist인자(i)가 n의 배수이면
          answer.append(i) # answer 리스트에 i를 추가하기
    return answer

n=int(input())
numlist=list(map(int,input().split()))
print(solution(n,numlist))