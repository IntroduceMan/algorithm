def solution(s):
    answer = 0
    numbers = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
    }
    keys = list(numbers.keys())
    for i in range(0,10):
        s = s.replace(keys[i], numbers[keys[i]])
    answer = int(s) # 정수형으로 형변환 한다.
    return answer

s = input()
print(solution(s))