# 홀수면 total//num 기준으로 양쪽으로 각각 (num-1)//2 개 만큼 연속나열
# 짝수면 total//num 기준으로 왼쪽은 (num//2)-1개, 오른쪽은 num//2개 만큼 연속 나열

def solution(num, total):
    answer = []
    mid = total // num
    if(num % 2): # 홀수이면
       for i in range(mid-(num-1)//2, mid+(num-1)//2+1):
          answer.append(i)
    else: # 짝수이면
       for i in range(mid-(num//2)+1,mid+(num//2)+1):
          answer.append(i)
    return answer

num, total = map(int,input().split())
print(solution(num,total))