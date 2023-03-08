def solution(num):
    count = 0
    while True:
        if num == 1:
            return count
        count += 1
        if num % 2 == True:
            num *= 3
            num += 1
        else:
            num /= 2
        if count == 500:
            return -1