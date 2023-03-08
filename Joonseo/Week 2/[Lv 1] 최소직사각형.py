def solution(sizes):
    answer = 0
    maxh = 0
    maxw = 0
    for rect in sizes:
       if (rect[0] < rect[1]):
          rect[0], rect[1] = rect[1], rect[0] # 스와프
       if (rect[0] > maxw):
          maxw = rect[0]
       if (rect[1] > maxh):
          maxh = rect[1]
    answer = maxh * maxw
    return answer

 