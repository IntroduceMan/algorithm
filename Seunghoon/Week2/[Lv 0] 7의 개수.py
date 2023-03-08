def solution(array):
    count = 0
    for i in array:
        for j in range(len(str(i))):
            if(str(i)[j] == '7'):  # 그냥 문자열로 했음.. 정수형엔 규칙이 없눙
                count += 1
            
    return count

solution