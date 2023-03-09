def solution(n, k):
    ser = 0
    t = n
    while t >= 10:
        ser += 1
        t-=10
    answer = n*12000 + (k-ser)*2000
    return answer