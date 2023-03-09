def solution(money):
    a = int(money/5500)#잔
    b = money-a*5500#거스름돈
    answer = [a, b]
    return answer