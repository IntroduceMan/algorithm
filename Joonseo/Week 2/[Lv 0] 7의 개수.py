def solution(array):
    answer = 0
    for num in array:
       numstr = str(num)
       for i in numstr:
          if (i=="7"):
             answer+=1
    return answer