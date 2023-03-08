def solution(common):
    answer = 0
    if(common[1] - common[0] == common[2] - common[1]): # 두번째수와 첫번째 수의 차와 두번째 수와 세번째 수의 차를 비교한다.
       answer = common[-1] + common[1] - common[0] # 만약 같다면 등차수열이고, answer는 맨 마지막 수에 그 차를 더한 값이다.
    else: # 아니라면 등비수열이다.
       answer = common[-1] * common[1] // common[0] # answer는 두번째 수 / 첫번째수 의 값을 맨 마지막 수에 곱한 값이다.
    return answer

common = list(map(int,input().split()))
print(solution(common))