def solution(numbers):
    answer = []
    for i in range(0, len(numbers) - 1): # 첫번째 인덱스부터 뒤에서 2번째 인덱스까지 순회하면서
       for j in range(i+1, len(numbers)): # i 이후의 값들을 순회한다
          if(numbers[i]+numbers[j] not in answer): # 만약 i인덱스와 j인덱스를 합한 값이 answer에 없으면
             answer.append(numbers[i]+numbers[j]) # answer에 합한 값을 삽입
    answer = sorted(answer) # answer을 정렬
    return answer

numbers = [2,1,3,4,1]	
print(solution(numbers))